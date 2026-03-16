"""
Image Handler Module
Handles downloading, caching, and processing images for the RSS reader
"""

import io
import os
import requests
from PIL import Image, ImageTk
from typing import Optional, Dict


class ImageHandler:
    """Manages image downloading, caching, and conversion for tkinter"""

    def __init__(self, cache_dir: str = "image_cache"):
        """
        Initialize ImageHandler

        Args:
            cache_dir: Directory to cache downloaded images
        """
        self.cache_dir = cache_dir
        self.image_cache: Dict[str, ImageTk.PhotoImage] = {}

        # Create cache directory if it doesn't exist
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

    def download_image(self, url: str, timeout: int = 10) -> Optional[Image.Image]:
        """
        Download image from URL

        Args:
            url: Image URL
            timeout: Request timeout in seconds

        Returns:
            PIL Image object or None if failed
        """
        try:
            response = requests.get(url, timeout=timeout, stream=True)
            response.raise_for_status()

            # Open image from response content
            image = Image.open(io.BytesIO(response.content))
            return image
        except Exception as e:
            print(f"Error downloading image from {url}: {e}")
            return None

    def resize_image(
        self, image: Image.Image, max_width: int, max_height: int
    ) -> Image.Image:
        """
        Resize image to fit within max dimensions while maintaining aspect ratio

        Args:
            image: PIL Image object
            max_width: Maximum width
            max_height: Maximum height

        Returns:
            Resized PIL Image object
        """
        # Calculate aspect ratio
        width, height = image.size
        aspect_ratio = width / height

        # Calculate new dimensions
        if width > height:
            new_width = min(width, max_width)
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = min(height, max_height)
            new_width = int(new_height * aspect_ratio)

        # Ensure dimensions don't exceed max
        if new_width > max_width:
            new_width = max_width
            new_height = int(new_width / aspect_ratio)

        if new_height > max_height:
            new_height = max_height
            new_width = int(new_height * aspect_ratio)

        # Resize image
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        return resized_image

    def get_thumbnail(
        self, url: str, size: tuple = (80, 60)
    ) -> Optional[ImageTk.PhotoImage]:
        """
        Get thumbnail image for table display

        Args:
            url: Image URL
            size: Thumbnail size (width, height)

        Returns:
            PhotoImage for tkinter or None if failed
        """
        cache_key = f"thumb_{url}"

        # Check cache first
        if cache_key in self.image_cache:
            return self.image_cache[cache_key]

        # Download and process image
        image = self.download_image(url)
        if image is None:
            return None

        # Resize to thumbnail
        thumbnail = self.resize_image(image, size[0], size[1])

        # Convert to PhotoImage
        photo_image = ImageTk.PhotoImage(thumbnail)

        # Cache it
        self.image_cache[cache_key] = photo_image

        return photo_image

    def get_preview_image(
        self, url: str, max_width: int = 500, max_height: int = 400
    ) -> Optional[ImageTk.PhotoImage]:
        """
        Get preview image for large display

        Args:
            url: Image URL
            max_width: Maximum preview width
            max_height: Maximum preview height

        Returns:
            PhotoImage for tkinter or None if failed
        """
        cache_key = f"preview_{url}"

        # Check cache first
        if cache_key in self.image_cache:
            return self.image_cache[cache_key]

        # Download and process image
        image = self.download_image(url)
        if image is None:
            return None

        # Resize for preview
        preview = self.resize_image(image, max_width, max_height)

        # Convert to PhotoImage
        photo_image = ImageTk.PhotoImage(preview)

        # Cache it
        self.image_cache[cache_key] = photo_image

        return photo_image

    def clear_cache(self):
        """Clear image cache"""
        self.image_cache.clear()
