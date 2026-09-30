def build_comic_layout(story_panels: list, image_paths: list) -> list:
    """
    Combines panel outlines, generated text, and generated images into a layout structure.
    """
    layout = []
    for story, img_path in zip(story_panels, image_paths):
        layout.append({
            "panel": story["panel"],
            "title": story["title"],
            "scene_description": story["scene_description"],
            "image_prompt": story["image_prompt"],
            "story_text": story["story_text"],
            "image_path": img_path
        })
    return layout