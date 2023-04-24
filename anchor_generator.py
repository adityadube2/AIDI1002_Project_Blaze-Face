class anchor_options:
    def __init__(self, feature_map_shape, aspect_ratios, scales, stride, base_anchor_size):
        self.feature_map_shape = feature_map_shape
        self.aspect_ratios = aspect_ratios
        self.scales = scales
        self.stride = stride
        self.base_anchor_size = base_anchor_size
