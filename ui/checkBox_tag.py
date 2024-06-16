from PySide6.QtCore import Signal
from PySide6.QtWidgets import QCheckBox


class CheckBoxTag(QCheckBox):
    signal_state_changed = Signal(str, bool)

    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.stateChanged.connect(self._emit_signal)

    def _emit_signal(self):
        text = self.text()
        is_checked = self.isChecked()
        self.signal_state_changed.emit(text, is_checked)
