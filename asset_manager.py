import os

from pathlib import Path
from enum import Enum

class AssetType(Enum):
    BACKGROUND = 1
    STATUS_CARDS = 2
    BUTTON_HOME = 3
    BUTTON_SETTINGS = 4
    ENTRY = 5

class AssetManager:
    def __init__(self):
        self.root_path = Path(__file__).absolute().parent
        self.assets_path = Path(os.path.join(self.root_path, "assets"))

    def get_path(self, asset_type: AssetType):
        match asset_type:
            case AssetType.BACKGROUND:
                return os.path.join(
                    self.assets_path,
                    "background.png"
                )
            case AssetType.STATUS_CARDS:
                return os.path.join(
                    self.assets_path,
                    "status_cards.png"
                )
            case AssetType.BUTTON_HOME:
                return os.path.join(
                    self.assets_path,
                    "button_home.png"
                )
            case AssetType.BUTTON_SETTINGS:
                return os.path.join(
                    self.assets_path,
                    "button_settings.png"
                )
            case AssetType.ENTRY:
                return os.path.join(
                    self.assets_path,
                    "entry.png"
                )