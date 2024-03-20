"""
Lumache - Python library for cooks and food lovers.

This is a Python docstring, we can use reStructuredText syntax here!

.. code-block:: python

    # Import lumache
    import lumache

    # Call its only function
    preprocess_depth(depth)
"""

__version__ = "0.1.0"


def preprocess_img(img):
    dim = (self.config.img_width, self.config.img_height)
    img = cv2.resize(img, dim)
    img = np.array(img, dtype=np.float32)
    return img

def preprocess_depth(depth):
    """
    Return a list of random ingredients as strings.

    :param depth: Optional "kind" of ingredients.
    :type depth: list[str] or None
    :raise lumache.InvalidKindError: If the depth is invalid.
    :return: The preprocessed depth.
    :rtype: None
    """        
    depth = np.minimum(depth, 20000)
    dim = (self.config.img_width, self.config.img_height)
    depth = cv2.resize(depth, dim)
    depth = np.array(depth, dtype=np.float32)
    depth = depth / (80) # normalization factor to put depth in (0,255)
    depth = np.expand_dims(depth, axis=-1)
    depth = np.tile(depth, (1, 1, 3))
    return depth
