"use client";

import Link from "next/link";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import cytoscape, { Core, EdgeSingular } from "cytoscape";
import dagre from "cytoscape-dagre";
import { find_path as findPath } from "dijkstrajs";
import { Graph } from "@/interface/common/grap.interface";
import { Play, RefreshCw, AlertCircle } from "lucide-react";

cytoscape.use(dagre);

interface PathResult {
  path: string[];
  distance: number;
}

export default function ShortestPathPage() {
  const containerRef = useRef<HTMLDivElement>(null);
  const cyRef = useRef<Core | null>(null);

  const [graphs, setGraphs] = useState<Graph[]>([]);
  const [selectedGraphId, setSelectedGraphId] = useState("");
  const [currentGraph, setCurrentGraph] = useState<Graph | null>(null);
  const [startNode, setStartNode] = useState("");
  const [endNode, setEndNode] = useState("");
  const [result, setResult] = useState<PathResult | null>(null);
  const [statusMessage, setStatusMessage] = useState("");
  const [isRunning, setIsRunning] = useState(false);
  const [loadingGraphs, setLoadingGraphs] = useState(true);

  const clearHighlights = useCallback(() => {
    const cy = cyRef.current;
    if (!cy) return;
    cy.nodes().removeClass("shortest-node");
    cy.edges().removeClass("shortest-edge");
  }, []);

  const loadGraphs = useCallback(() => {
    setLoadingGraphs(true);
    try {
      const stored = JSON.parse(
        localStorage.getItem("graphs") || "[]"
      ) as Graph[];
      const usable = stored.filter(
        (graph) =>
          graph?.data?.nodes?.length &&
          graph?.data?.edges &&
          Array.isArray(graph.data.nodes)
      );
      setGraphs(usable);
    } catch (error) {
      console.error("Failed to load graphs:", error);
      setGraphs([]);
    } finally {
      setLoadingGraphs(false);
    }
  }, []);

  useEffect(() => {
    loadGraphs();
    const handleStorage = () => loadGraphs();
    window.addEventListener("storage", handleStorage);
    return () => window.removeEventListener("storage", handleStorage);
  }, [loadGraphs]);

  useEffect(() => {
    if (!graphs.length) {
      setSelectedGraphId("");
      setCurrentGraph(null);
      return;
    }
    if (!selectedGraphId || !graphs.some((g) => g.id === selectedGraphId)) {
      setSelectedGraphId(graphs[0].id);
      return;
    }
    const found = graphs.find((graph) => graph.id === selectedGraphId) ?? null;
    setCurrentGraph(found?.data ? found : null);
  }, [graphs, selectedGraphId]);

  useEffect(() => {
    if (!currentGraph?.data?.nodes?.length) {
      setStartNode("");
      setEndNode("");
      setResult(null);
      setStatusMessage("");
      clearHighlights();
      return;
    }

    const nodes = currentGraph.data.nodes;
    setStartNode(nodes[0].id);
    setEndNode(nodes[nodes.length > 1 ? 1 : 0].id);
    setResult(null);
    setStatusMessage("");
    clearHighlights();
  }, [currentGraph, clearHighlights]);

  useEffect(() => {
    if (!containerRef.current || cyRef.current) return;

    const cy = cytoscape({
      container: containerRef.current,
      elements: [],
      style: [
        {
          selector: "node",
          style: {
            "background-color": "#4F46E5",
            "border-color": "#312E81",
            "border-width": 2,
            label: "data(label)",
            color: "#FFFFFF",
            "text-valign": "center",
            "text-halign": "center",
            "font-size": 14,
            width: 44,
            height: 44,
          },
        },
        {
          selector: ".shortest-node",
          style: {
            "background-color": "#10B981",
            "border-color": "#047857",
            width: 48,
            height: 48,
            "font-weight": "bold",
          },
        },
        {
          selector: "edge",
          style: {
            width: 3,
            "line-color": "#94A3B8",
            "target-arrow-color": "#94A3B8",
            "target-arrow-shape": "none",
            "curve-style": "bezier",
            "control-point-distance": (ele: EdgeSingular) =>
              ele.data("curveDistance") || 0,
            label: (ele: EdgeSingular) => ele.data("displayWeight") ?? "",
            "text-background-color": "#FFFFFF",
            "text-background-opacity": 0.8,
            "text-background-shape": "roundrectangle",
            "text-background-padding": "2px",
            "font-size": 12,
            color: "#1F2937",
          },
        },
        {
          selector: ".shortest-edge",
          style: {
            "line-color": "#F59E0B",
            "target-arrow-color": "#F59E0B",
            width: 5,
          },
        },
      ],
      layout: { name: "preset" },
      wheelSensitivity: 0.2,
      minZoom: 0.2,
      maxZoom: 3,
    });

    cyRef.current = cy;

    return () => {
      cy.destroy();
      cyRef.current = null;
    };
  }, []);

  useEffect(() => {
    const cy = cyRef.current;
    if (!cy) return;
    cy.elements().remove();
    if (!currentGraph?.data) return;

    const hasPreset = currentGraph.data.nodes.every(
      (node) => typeof node.x === "number" && typeof node.y === "number"
    );

    const nodes = currentGraph.data.nodes.map((node) => ({
      data: node,
      position:
        typeof node.x === "number" && typeof node.y === "number"
          ? { x: node.x, y: node.y }
          : undefined,
    }));

    const edges = currentGraph.data.edges.map((edge) => ({
      data: {
        ...edge,
        displayWeight: currentGraph.weighted
          ? typeof edge.weight === "number"
            ? edge.weight
            : 1
          : "",
        curveDistance: edge.curveDistance ?? 0,
      },
    }));

    cy.add([...nodes, ...edges]);
    cy.layout({
      name: hasPreset ? "preset" : "dagre",
      fit: true,
      padding: 60,
    }).run();

    cy.edges().style(
      "target-arrow-shape",
      currentGraph.type === "directed" ? "triangle" : "none"
    );
    clearHighlights();
  }, [currentGraph, clearHighlights]);

  const hasNegativeWeights = useMemo(
    () =>
      currentGraph?.data?.edges?.some(
        (edge) => typeof edge.weight === "number" && edge.weight < 0
      ) ?? false,
    [currentGraph]
  );

  const buildAdjacency = useCallback((graph: Graph) => {
    const adjacency: Record<string, Record<string, number>> = {};
    const nodes = graph.data?.nodes ?? [];
    nodes.forEach((node) => {
      adjacency[node.id] = {};
    });

    const edges = graph.data?.edges ?? [];
    edges.forEach((edge) => {
      const weight = typeof edge.weight === "number" ? edge.weight : 1;
      if (!adjacency[edge.source]) adjacency[edge.source] = {};
      adjacency[edge.source][edge.target] = weight;
      if (graph.type !== "directed") {
        if (!adjacency[edge.target]) adjacency[edge.target] = {};
        adjacency[edge.target][edge.source] = weight;
      }
    });

    return adjacency;
  }, []);

  const runDijkstraWithLibrary = useCallback(
    (graph: Graph, startId: string, endId: string): PathResult => {
      if (!graph.data?.nodes?.length) {
        return { path: [], distance: Infinity };
      }

      const nodes = graph.data.nodes;
      if (
        !nodes.some((node) => node.id === startId) ||
        !nodes.some((node) => node.id === endId)
      ) {
        return { path: [], distance: Infinity };
      }

      try {
        const adjacency = buildAdjacency(graph);
        const path = findPath(adjacency, startId, endId);

        if (!Array.isArray(path) || path.length === 0) {
          return { path: [], distance: Infinity };
        }

        const totalDistance = path.slice(0, -1).reduce((sum, nodeId, index) => {
          const next = path[index + 1];
          const weight = adjacency[nodeId]?.[next];
          if (typeof weight !== "number") {
            return Infinity;
          }
          return sum + weight;
        }, 0);

        if (!Number.isFinite(totalDistance)) {
          return { path: [], distance: Infinity };
        }

        return { path, distance: totalDistance };
      } catch (error) {
        console.warn("Dijkstra library error", error);
        return { path: [], distance: Infinity };
      }
    },
    [buildAdjacency]
  );

  const highlightPath = useCallback(
    (path: string[], graph: Graph) => {
      const cy = cyRef.current;
      if (!cy || !path.length) return;

      clearHighlights();
      path.forEach((nodeId) => {
        const node = cy.$id(nodeId);
        if (node) node.addClass("shortest-node");
      });

      if (path.length < 2) return;

      for (let i = 0; i < path.length - 1; i++) {
        const from = path[i];
        const to = path[i + 1];
        const edges = cy.edges().filter((edge) => {
          const source = edge.data("source");
          const target = edge.data("target");
          if (graph.type === "directed") {
            return source === from && target === to;
          }
          return (
            (source === from && target === to) ||
            (source === to && target === from)
          );
        });
        edges.addClass("shortest-edge");
      }
    },
    [clearHighlights]
  );

  const handleRun = () => {
    if (!currentGraph?.data) {
      setStatusMessage("Chưa có đồ thị để chạy thuật toán.");
      return;
    }
    if (!startNode || !endNode) {
      setStatusMessage("Hãy chọn đỉnh bắt đầu và kết thúc.");
      return;
    }
    if (hasNegativeWeights) {
      setStatusMessage(
        "Dijkstra không hỗ trợ trọng số âm. Hãy chỉnh sửa đồ thị."
      );
      return;
    }

    setIsRunning(true);
    setStatusMessage("");

    const outcome = runDijkstraWithLibrary(currentGraph, startNode, endNode);
    setIsRunning(false);

    if (!outcome.path.length) {
      setResult(null);
      setStatusMessage("Không tìm thấy đường đi giữa hai đỉnh đã chọn.");
      clearHighlights();
      return;
    }

    setResult(outcome);
    highlightPath(outcome.path, currentGraph);
  };

  const nodeOptions = currentGraph?.data?.nodes ?? [];
  const edgeCount = currentGraph?.data?.edges?.length ?? 0;

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-white py-8">
      <div className="container mx-auto px-4 space-y-6 max-w-6xl">
        <div className="bg-white rounded-2xl shadow-sm p-6 flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
          <div>
            <p className="text-sm font-semibold text-blue-600 uppercase tracking-wide">
              Thuật toán
            </p>
            <h1 className="text-3xl font-bold text-gray-900 mt-1">
              1. Tìm đường đi ngắn nhất (Dijkstra)
            </h1>
            <p className="text-gray-600 mt-2">
              Chọn đồ thị bạn đã vẽ, xác định đỉnh bắt đầu/kết thúc và hệ thống
              sẽ highlight đường đi ngắn nhất ngay trên đồ thị đó.
            </p>
          </div>
          <div className="flex flex-wrap gap-2">
            <button
              onClick={loadGraphs}
              className="flex items-center gap-2 px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition-colors"
              aria-label="Tải lại danh sách đồ thị"
              title="Tải lại danh sách"
            >
              <RefreshCw size={18} />
              Tải lại danh sách
            </button>
            <Link
              href="/graph/create"
              className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
            >
              Vẽ đồ thị mới
            </Link>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="bg-white rounded-2xl shadow-sm p-6 space-y-5">
            <div>
              <label
                htmlFor="graph-select"
                className="block text-sm font-medium text-gray-700 mb-1"
              >
                Đồ thị đã lưu
              </label>
              <select
                id="graph-select"
                value={selectedGraphId}
                onChange={(e) => setSelectedGraphId(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
              >
                {graphs.map((graph) => (
                  <option key={graph.id} value={graph.id}>
                    {graph.name}
                  </option>
                ))}
              </select>
              {loadingGraphs && (
                <p className="text-xs text-gray-500 mt-1">
                  Đang tải danh sách...
                </p>
              )}
              {!loadingGraphs && !graphs.length && (
                <p className="text-xs text-red-500 mt-1">
                  Chưa có đồ thị nào. Hãy tạo mới trong mục &quot;Đồ thị&quot;.
                </p>
              )}
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label
                  htmlFor="start-node-select"
                  className="block text-sm font-medium text-gray-700 mb-1"
                >
                  Đỉnh bắt đầu
                </label>
                <select
                  id="start-node-select"
                  value={startNode}
                  onChange={(e) => setStartNode(e.target.value)}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  disabled={!nodeOptions.length}
                >
                  {nodeOptions.map((node) => (
                    <option key={node.id} value={node.id}>
                      {node.label || node.id}
                    </option>
                  ))}
                </select>
              </div>
              <div>
                <label
                  htmlFor="end-node-select"
                  className="block text-sm font-medium text-gray-700 mb-1"
                >
                  Đỉnh kết thúc
                </label>
                <select
                  id="end-node-select"
                  value={endNode}
                  onChange={(e) => setEndNode(e.target.value)}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                  disabled={!nodeOptions.length}
                >
                  {nodeOptions.map((node) => (
                    <option key={node.id} value={node.id}>
                      {node.label || node.id}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            {currentGraph && (
              <div className="grid grid-cols-2 gap-3 bg-gray-50 border border-gray-100 rounded-xl p-3 text-sm">
                <div>
                  <p className="text-gray-500">Loại</p>
                  <p className="font-semibold text-gray-800">
                    {currentGraph.type === "directed" ? "Có hướng" : "Vô hướng"}
                  </p>
                </div>
                <div>
                  <p className="text-gray-500">Trọng số</p>
                  <p className="font-semibold text-gray-800">
                    {currentGraph.weighted ? "Có" : "Không"}
                  </p>
                </div>
                <div>
                  <p className="text-gray-500">Số đỉnh</p>
                  <p className="font-semibold text-gray-800">
                    {nodeOptions.length}
                  </p>
                </div>
                <div>
                  <p className="text-gray-500">Số cạnh</p>
                  <p className="font-semibold text-gray-800">{edgeCount}</p>
                </div>
              </div>
            )}

            {hasNegativeWeights && (
              <div className="flex items-start gap-2 rounded-lg border border-amber-200 bg-amber-50 px-3 py-2 text-sm text-amber-800">
                <AlertCircle size={18} className="mt-0.5" />
                <p>
                  Đồ thị có trọng số âm. Dijkstra yêu cầu trọng số không âm, vui
                  lòng chỉnh sửa đồ thị.
                </p>
              </div>
            )}

            {statusMessage && (
              <div className="flex items-start gap-2 rounded-lg border border-red-200 bg-red-50 px-3 py-2 text-sm text-red-700">
                <AlertCircle size={18} className="mt-0.5" />
                <p>{statusMessage}</p>
              </div>
            )}

            <button
              onClick={handleRun}
              disabled={
                isRunning ||
                !currentGraph ||
                !startNode ||
                !endNode ||
                hasNegativeWeights
              }
              className="w-full flex items-center âjustify-center gap-2 px-4 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <Play size={18} />
              {isRunning ? "Đang chạy Dijkstra..." : "Chạy Dijkstra"}
            </button>
          </div>

          <div className="lg:col-span-2 bg-white rounded-2xl shadow-sm p-6 space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <h2 className="text-xl font-semibold text-gray-900">
                  Đồ thị trực quan
                </h2>
                <p className="text-sm text-gray-500">
                  Highlight đường đi ngắn nhất sẽ xuất hiện trực tiếp ở đây.
                </p>
              </div>
              {currentGraph && (
                <p className="text-sm text-gray-500">
                  Cập nhật lần cuối:{" "}
                  {new Date(currentGraph.updatedAt).toLocaleString()}
                </p>
              )}
            </div>

            <div
              ref={containerRef}
              className="w-full border border-gray-200 rounded-xl h-[520px] bg-gray-50"
            ></div>

            {result && (
              <div className="rounded-xl border border-blue-100 bg-blue-50 px-4 py-3">
                <p className="text-sm font-semibold text-blue-800">Kết quả</p>
                <div className="flex flex-wrap gap-4 mt-2 text-sm">
                  <div>
                    <p className="text-gray-500">Đường đi</p>
                    <p className="font-mono text-gray-900">
                      {result.path.join(" → ")}
                    </p>
                  </div>
                  <div>
                    <p className="text-gray-500">Khoảng cách</p>
                    <p className="font-semibold text-gray-900">
                      {result.distance}
                    </p>
                  </div>
                  <div>
                    <p className="text-gray-500">Số đỉnh</p>
                    <p className="font-semibold text-gray-900">
                      {result.path.length}
                    </p>
                  </div>
                </div>
              </div>
            )}

            {!currentGraph && !graphs.length && !loadingGraphs && (
              <div className="rounded-xl border border-dashed border-gray-300 p-6 text-center text-gray-500">
                Chưa có đồ thị nào để chạy thuật toán. Hãy tạo đồ thị mới trong
                mục &quot;Đồ thị&quot;.
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
