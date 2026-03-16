"""
RSS Parser Module
Handles fetching and parsing RSS feeds from VNExpress
"""

import feedparser
from datetime import datetime
from typing import List, Dict, Optional


class RSSParser:
    """Parses VNExpress RSS feeds"""

    # VNExpress RSS feed URLs mapped by category
    CATEGORY_URLS = {
        "Cười": "https://vnexpress.net/rss/cuoi.rss",
        "Thời sự": "https://vnexpress.net/rss/thoi-su.rss",
        "Góc nhìn": "https://vnexpress.net/rss/goc-nhin.rss",
        "Thế giới": "https://vnexpress.net/rss/the-gioi.rss",
        "Kinh doanh": "https://vnexpress.net/rss/kinh-doanh.rss",
        "Giải trí": "https://vnexpress.net/rss/giai-tri.rss",
        "Thể thao": "https://vnexpress.net/rss/the-thao.rss",
        "Pháp luật": "https://vnexpress.net/rss/phap-luat.rss",
        "Giáo dục": "https://vnexpress.net/rss/giao-duc.rss",
        "Sức khỏe": "https://vnexpress.net/rss/suc-khoe.rss",
        "Gia đình": "https://vnexpress.net/rss/gia-dinh.rss",
        "Du lịch": "https://vnexpress.net/rss/du-lich.rss",
        "Khoa học": "https://vnexpress.net/rss/khoa-hoc.rss",
        "Số hóa": "https://vnexpress.net/rss/so-hoa.rss",
        "Xe": "https://vnexpress.net/rss/xe.rss",
        "Ý kiến": "https://vnexpress.net/rss/y-kien.rss",
        "Tâm sự": "https://vnexpress.net/rss/tam-su.rss",
    }

    @classmethod
    def get_categories(cls) -> List[str]:
        """
        Get list of available categories

        Returns:
            List of category names
        """
        return list(cls.CATEGORY_URLS.keys())

    @classmethod
    def fetch_feed(cls, category: str) -> List[Dict[str, str]]:
        """
        Fetch and parse RSS feed for given category

        Args:
            category: Category name

        Returns:
            List of article dictionaries with keys: title, summary, image, published, link
        """
        if category not in cls.CATEGORY_URLS:
            raise ValueError(f"Invalid category: {category}")

        url = cls.CATEGORY_URLS[category]

        try:
            # Parse RSS feed
            feed = feedparser.parse(url)

            articles = []
            for entry in feed.entries:
                article = cls._parse_entry(entry)
                if article:
                    articles.append(article)

            return articles

        except Exception as e:
            print(f"Error fetching RSS feed: {e}")
            return []

    @classmethod
    def _parse_entry(cls, entry) -> Optional[Dict[str, str]]:
        """
        Parse a single RSS entry

        Args:
            entry: Feed entry object

        Returns:
            Article dictionary or None if parsing failed
        """
        try:
            # Extract title
            title = entry.get("title", "No title")

            # Extract summary/description
            summary = entry.get("summary", entry.get("description", "No summary"))
            # Clean HTML tags from summary
            summary = cls._clean_html(summary)

            # Extract image URL
            image_url = cls._extract_image(entry)

            # Extract published date
            published = cls._format_date(entry.get("published", ""))

            # Extract link
            link = entry.get("link", "")

            return {
                "title": title,
                "summary": summary,
                "image": image_url,
                "published": published,
                "link": link,
            }

        except Exception as e:
            print(f"Error parsing entry: {e}")
            return None

    @classmethod
    def _extract_image(cls, entry) -> str:
        """
        Extract image URL from entry

        Args:
            entry: Feed entry object

        Returns:
            Image URL or empty string
        """
        # Try to get image from media content
        if hasattr(entry, "media_content") and entry.media_content:
            return entry.media_content[0].get("url", "")

        # Try to get image from enclosures
        if hasattr(entry, "enclosures") and entry.enclosures:
            for enclosure in entry.enclosures:
                if enclosure.get("type", "").startswith("image"):
                    return enclosure.get("href", "")

        # Try to extract from description/summary
        if hasattr(entry, "description"):
            import re

            img_match = re.search(r'<img[^>]+src="([^"]+)"', entry.description)
            if img_match:
                return img_match.group(1)

        return ""

    @classmethod
    def _clean_html(cls, text: str) -> str:
        """
        Remove HTML tags from text

        Args:
            text: Text with HTML tags

        Returns:
            Clean text
        """
        import re

        # Remove HTML tags
        clean = re.sub(r"<[^>]+>", "", text)
        # Remove extra whitespace
        clean = " ".join(clean.split())
        return clean

    @classmethod
    def _format_date(cls, date_str: str) -> str:
        """
        Format date string to Vietnamese format

        Args:
            date_str: Date string from RSS feed

        Returns:
            Formatted date string (DD/MM/YYYY HH:MM)
        """
        if not date_str:
            return ""

        try:
            # Parse date
            dt = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")
            # Format to Vietnamese style
            return dt.strftime("%d/%m/%Y %H:%M")
        except:
            try:
                # Try alternative format
                from dateutil import parser

                dt = parser.parse(date_str)
                return dt.strftime("%d/%m/%Y %H:%M")
            except:
                return date_str
