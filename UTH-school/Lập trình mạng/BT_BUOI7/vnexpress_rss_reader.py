"""
VNExpress RSS Reader
Main GUI application for reading VNExpress RSS feeds
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from typing import List, Dict, Optional
import threading
import requests
from bs4 import BeautifulSoup

from rss_parser import RSSParser
from image_handler import ImageHandler


class VNExpressRSSReader:
    """Main application class for VNExpress RSS Reader"""

    def __init__(self, root: tk.Tk):
        """Initialize the application"""
        self.root = root
        self.image_handler = ImageHandler()
        self.articles: List[Dict] = []
        self.filtered_articles: List[Dict] = []
        self.current_selection: Optional[int] = None
        self.current_article_link: str = ""

        self.setup_window()
        self.create_widgets()
        self.update_status("Ready.")

    def setup_window(self):
        """Setup main window properties"""
        # Set window title with current date
        current_date = datetime.now().strftime("%Y-%m-%d")
        self.root.title(f"VnExpress RSS Reader ({current_date})")

        # Set window size
        self.root.geometry("1000x650")
        self.root.minsize(900, 600)

        # Configure grid weights
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def create_widgets(self):
        """Create all GUI widgets"""
        # Top control panel
        self.create_control_panel()

        # Main content area (table + image preview)
        self.create_main_content()

        # Status bar
        self.create_status_bar()

    def create_control_panel(self):
        """Create top control panel with category, search, and buttons"""
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.grid(row=0, column=0, sticky="ew")

        # Category selection
        ttk.Label(control_frame, text="Select Category:").grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )

        self.category_var = tk.StringVar(value="Cười")
        self.category_combo = ttk.Combobox(
            control_frame,
            textvariable=self.category_var,
            values=RSSParser.get_categories(),
            state="readonly",
            width=20,
        )
        self.category_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Load Feed button
        self.load_button = ttk.Button(
            control_frame, text="Load Feed", command=self.load_feed
        )
        self.load_button.grid(row=0, column=2, padx=5, pady=5)

        # Search
        ttk.Label(control_frame, text="Search:").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )

        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *args: self.filter_articles())

        self.search_entry = ttk.Entry(
            control_frame, textvariable=self.search_var, width=30
        )
        self.search_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Clear Search button
        self.clear_button = ttk.Button(
            control_frame, text="Clear Search", command=self.clear_search
        )
        self.clear_button.grid(row=1, column=2, padx=5, pady=5)

        # Configure column weights
        control_frame.grid_columnconfigure(1, weight=1)

    def create_main_content(self):
        """Create main content area with table and image preview"""
        # Create main paned window for resizable split
        main_paned = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_paned.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        # Left side: Article table
        self.create_article_table(main_paned)

        # Right side: Image preview
        self.create_image_preview(main_paned)

    def create_article_table(self, parent):
        """Create article table with scrollbars"""
        # Frame for table
        table_frame = ttk.Frame(parent)
        parent.add(table_frame, weight=6)

        # Create Treeview for article table
        columns = ("no", "title", "summary", "published")
        self.article_tree = ttk.Treeview(
            table_frame, columns=columns, show="headings", selectmode="browse"
        )

        # Define column headings
        self.article_tree.heading("no", text="No.")
        self.article_tree.heading("title", text="Title")
        self.article_tree.heading("summary", text="Summary")
        self.article_tree.heading("published", text="Published")

        # Define column widths
        self.article_tree.column("no", width=50, minwidth=40, stretch=False)
        self.article_tree.column("title", width=250, minwidth=150)
        self.article_tree.column("summary", width=400, minwidth=200)
        self.article_tree.column("published", width=140, minwidth=100)

        # Configure row height
        style = ttk.Style()
        style.configure("Treeview", rowheight=25)

        # Scrollbars
        vsb = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.article_tree.yview
        )
        hsb = ttk.Scrollbar(
            table_frame, orient="horizontal", command=self.article_tree.xview
        )
        self.article_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Grid layout
        self.article_tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        # Configure grid weights
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        # Bind selection event
        self.article_tree.bind("<<TreeviewSelect>>", self.on_article_select)

    def create_image_preview(self, parent):
        """Create article preview panel with web-style layout"""
        # Frame for article preview
        preview_frame = ttk.Frame(parent)
        parent.add(preview_frame, weight=4)

        # Configure grid
        preview_frame.grid_rowconfigure(0, weight=0)  # Title area
        preview_frame.grid_rowconfigure(1, weight=1)  # Content area (scrollable)
        preview_frame.grid_rowconfigure(2, weight=0)  # Bottom buttons
        preview_frame.grid_columnconfigure(0, weight=1)

        # Title Label (at top)
        self.preview_title = tk.Label(
            preview_frame,
            text="",
            font=("Arial", 16, "bold"),
            wraplength=450,
            justify=tk.LEFT,
            anchor="w",
            bg="#f0f0f0",
            padx=15,
            pady=10,
        )
        self.preview_title.grid(row=0, column=0, sticky="ew", padx=5, pady=(5, 0))

        # Scrollable content frame
        content_container = ttk.Frame(preview_frame)
        content_container.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        content_container.grid_rowconfigure(0, weight=1)
        content_container.grid_columnconfigure(0, weight=1)

        # Text widget for article content (can embed images)
        self.content_text = tk.Text(
            content_container,
            wrap=tk.WORD,
            font=("Arial", 11),
            bg="white",
            relief=tk.SOLID,
            borderwidth=1,
            padx=15,
            pady=10,
            spacing1=5,
            spacing3=5,
        )
        self.content_text.grid(row=0, column=0, sticky="nsew")

        # Scrollbar for content
        content_scrollbar = ttk.Scrollbar(
            content_container, orient="vertical", command=self.content_text.yview
        )
        content_scrollbar.grid(row=0, column=1, sticky="ns")
        self.content_text.configure(yscrollcommand=content_scrollbar.set)

        # Make text widget read-only
        self.content_text.config(state="disabled")

        # Configure text tags for formatting
        self.content_text.tag_configure("center", justify="center")
        self.content_text.tag_configure("date", foreground="gray", font=("Arial", 9))

        # Placeholder text
        self.content_text.config(state="normal")
        self.content_text.insert(
            "1.0", "Chọn một bài viết để xem chi tiết...", "center"
        )
        self.content_text.config(state="disabled")

        # Bottom section - Link button
        bottom_frame = ttk.Frame(preview_frame)
        bottom_frame.grid(row=2, column=0, sticky="ew", padx=5, pady=(0, 5))

        self.link_button = ttk.Button(
            bottom_frame,
            text="🔗 Mở bài viết gốc trên VNExpress",
            command=self.open_article_link,
            state="disabled",
        )
        self.link_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Store current article link
        self.current_article_link = ""

    def create_status_bar(self):
        """Create status bar at bottom"""
        self.status_bar = ttk.Label(
            self.root, text="Ready.", relief=tk.SUNKEN, anchor=tk.W, padding="5"
        )
        self.status_bar.grid(row=2, column=0, sticky="ew")

    def update_status(self, message: str):
        """Update status bar message"""
        self.status_bar.config(text=message)
        self.root.update_idletasks()

    def load_feed(self):
        """Load RSS feed for selected category"""
        category = self.category_var.get()

        if not category:
            messagebox.showwarning("Warning", "Please select a category")
            return

        # Disable load button during loading
        self.load_button.config(state="disabled")
        self.update_status(f"Loading {category} feed...")

        # Load feed in background thread
        thread = threading.Thread(target=self._load_feed_thread, args=(category,))
        thread.daemon = True
        thread.start()

    def _load_feed_thread(self, category: str):
        """Thread function to load RSS feed"""
        try:
            # Fetch articles
            articles = RSSParser.fetch_feed(category)

            # Update UI in main thread
            self.root.after(0, self._update_articles, articles)

        except Exception as e:
            error_msg = f"Error loading feed: {str(e)}"
            self.root.after(0, messagebox.showerror, "Error", error_msg)
            self.root.after(0, self.update_status, "Ready.")
            self.root.after(0, lambda: self.load_button.config(state="normal"))

    def _update_articles(self, articles: List[Dict]):
        """Update article list and display in table"""
        self.articles = articles
        self.filtered_articles = articles.copy()

        # Clear current table
        for item in self.article_tree.get_children():
            self.article_tree.delete(item)

        # Clear image cache for new feed
        self.image_handler.clear_cache()

        if not articles:
            self.update_status("No articles found.")
            self.load_button.config(state="normal")
            messagebox.showinfo("Info", "No articles found in this feed.")
            return

        # Add articles to table
        self.populate_table(articles)

        self.update_status(f"Loaded {len(articles)} articles.")
        self.load_button.config(state="normal")

    def populate_table(self, articles: List[Dict]):
        """Populate table with articles"""
        for idx, article in enumerate(articles, start=1):
            # Insert row
            item_id = self.article_tree.insert(
                "",
                "end",
                values=(
                    idx,
                    article.get("title", ""),
                    (
                        article.get("summary", "")[:200] + "..."
                        if len(article.get("summary", "")) > 200
                        else article.get("summary", "")
                    ),  # Truncate summary
                    article.get("published", ""),
                ),
                tags=(str(idx - 1),),  # Store article index in tags
            )

    def filter_articles(self):
        """Filter articles based on search query"""
        query = self.search_var.get().lower().strip()

        # Clear current table
        for item in self.article_tree.get_children():
            self.article_tree.delete(item)

        if not query:
            # Show all articles
            self.filtered_articles = self.articles.copy()
        else:
            # Filter articles
            self.filtered_articles = [
                article
                for article in self.articles
                if query in article.get("title", "").lower()
                or query in article.get("summary", "").lower()
            ]

        # Repopulate table
        self.populate_table(self.filtered_articles)

        # Update status
        if query:
            self.update_status(
                f"Found {len(self.filtered_articles)} articles matching '{query}'"
            )
        else:
            self.update_status(f"Showing {len(self.filtered_articles)} articles.")

    def clear_search(self):
        """Clear search field"""
        self.search_var.set("")
        self.search_entry.focus()

    def on_article_select(self, event):
        """Handle article selection in table"""
        selection = self.article_tree.selection()

        if not selection:
            return

        # Get selected item
        item = selection[0]
        tags = self.article_tree.item(item, "tags")

        if not tags:
            return

        # Get article index
        article_idx = int(tags[0])

        # Update image preview
        self.update_image_preview(article_idx)

    def update_image_preview(self, article_idx: int):
        """Update article preview with web-style layout"""
        if article_idx >= len(self.filtered_articles):
            return

        article = self.filtered_articles[article_idx]

        # Update title
        title = article.get("title", "No title")
        self.preview_title.config(text=title)

        # Update link
        self.current_article_link = article.get("link", "")
        if self.current_article_link:
            self.link_button.config(state="normal")
        else:
            self.link_button.config(state="disabled")

        # Clear content
        self.content_text.config(state="normal")
        self.content_text.delete("1.0", tk.END)

        # Get article data
        image_url = article.get("image", "")
        article_link = article.get("link", "")
        published = article.get("published", "Unknown date")

        # Show loading message
        self.content_text.insert("1.0", "Đang tải nội dung đầy đủ...\n\n")
        self.content_text.config(state="disabled")

        # Load full article content in background
        thread = threading.Thread(
            target=self._load_full_article, args=(image_url, article_link, published)
        )
        thread.daemon = True
        thread.start()

    def _load_full_article(self, image_url: str, article_link: str, published: str):
        """Load full article content from VNExpress page"""
        try:
            # Fetch full content from article page
            full_content = self._fetch_article_content(article_link)

            # Load image if available
            image = None
            if image_url:
                image = self.image_handler.get_preview_image(
                    image_url, max_width=400, max_height=300
                )

            # Update UI in main thread
            self.root.after(
                0, self._insert_article_content, image, full_content, published
            )

        except Exception as e:
            print(f"Error loading full article: {e}")
            # Fallback to summary if fetching fails
            article_idx = self.current_selection
            if article_idx is not None and article_idx < len(self.filtered_articles):
                summary = self.filtered_articles[article_idx].get(
                    "summary", "Không thể tải nội dung"
                )
                self.root.after(
                    0, self._insert_article_content, None, summary, published
                )

    def _fetch_article_content(self, url: str) -> str:
        """Fetch full article content from VNExpress page"""
        if not url:
            return "Không có link bài viết"

        try:
            # Fetch page
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            # Parse HTML
            soup = BeautifulSoup(response.content, "html.parser")

            # Find article content (VNExpress specific selectors)
            # Main content is usually in class 'fck_detail' or 'article-content'
            content_div = soup.find("article", class_="fck_detail")
            if not content_div:
                content_div = soup.find("div", class_="fck_detail")
            if not content_div:
                content_div = soup.find("div", class_="article-content")

            if content_div:
                # Extract text from paragraphs
                paragraphs = content_div.find_all("p", class_="Normal")
                if not paragraphs:
                    paragraphs = content_div.find_all("p")

                # Join all paragraphs
                full_text = "\n\n".join(
                    [
                        p.get_text(strip=True)
                        for p in paragraphs
                        if p.get_text(strip=True)
                    ]
                )

                if full_text:
                    return full_text

            # Fallback: try to get any text content
            return "Không thể trích xuất nội dung từ trang này"

        except Exception as e:
            print(f"Error fetching article content: {e}")
            return f"Lỗi khi tải nội dung: {str(e)}"

    def _insert_article_content(self, image, summary: str, published: str):
        """Insert article content into Text widget"""
        # Enable editing
        self.content_text.config(state="normal")
        self.content_text.delete("1.0", tk.END)

        # Insert image if available
        if image:
            # Insert image centered
            self.content_text.insert("1.0", "\n")
            self.content_text.image_create("1.0", image=image)
            self.content_text.insert("1.0", "\n")

            # Keep reference to prevent garbage collection
            if not hasattr(self, "_article_images"):
                self._article_images = []
            self._article_images.append(image)

            # Limit cache size
            if len(self._article_images) > 5:
                self._article_images.pop(0)

        # Insert published date
        self.content_text.insert(tk.END, f"\n📅 {published}\n\n", "date")

        # Insert summary/content
        self.content_text.insert(tk.END, summary)

        # Add some spacing at the end
        self.content_text.insert(tk.END, "\n\n")

        # Make read-only
        self.content_text.config(state="disabled")

        # Scroll to top
        self.content_text.see("1.0")

    def open_article_link(self):
        """Open article link in web browser"""
        if self.current_article_link:
            import webbrowser

            try:
                webbrowser.open(self.current_article_link)
            except Exception as e:
                messagebox.showerror("Error", f"Could not open link: {str(e)}")


def main():
    """Main entry point"""
    root = tk.Tk()
    app = VNExpressRSSReader(root)
    root.mainloop()


if __name__ == "__main__":
    main()
