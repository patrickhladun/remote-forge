def make_metadata(request, page):
    """
    Generate metadata for a webpage, including title, meta tags, and link tags.

    Args:
        request (HttpRequest): The HTTP request object.
        page (dict): A dictionary containing page metadata information. It
        should include:
            - "title": The title of the page.
            - "meta": A dictionary of meta tags (e.g., description, keywords).
            - "link": A dictionary of link tags (e.g., canonical).

    Returns:
        list: A list of HTML metadata tags.
    """
    site_name = "Remote Forge"
    url = request.build_absolute_uri()
    metadata = []

    title = f'{page["title"]} | {site_name}' if page["title"] else site_name
    metadata.append(f"<title>{title}</title>")

    if "meta" in page:
        for key, value in page["meta"].items():
            if value:
                metadata.append(f'<meta name="{key}" content="{value}">')
    if "link" in page:
        if "canonical" not in page.get("link", {}):
            metadata.append(f'<link rel="canonical" href="{url}">')

        for key, value in page["link"].items():
            if key == "canonical" and not value:
                metadata.append(f'<link rel="canonical" href="{url}">')
            elif key == "canonical" and value:
                metadata.append(f'<link rel="canonical" href="{value}">')
            else:
                metadata.append(f'<link rel="{key}" href="{value}">')
    else:
        metadata.append(f'<link rel="canonical" href="{url}">')

    return metadata
