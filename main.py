import os

from PySide6.QtGui import QPalette, QColor, QIcon, QPixmap, Qt, QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QMainWindow, QApplication, QInputDialog, QListWidgetItem, QMessageBox

from constant import _ICON_ADD, _ICON_DELETE, _ICON_RESTORE, _ICON_CONFIRM, _ICON_CLEAR, _ICON_DOWN, _IDENTIFIER, \
    _ICON_TAG
from module import function_config, function_normal
from ui.checkBox_tag import CheckBoxTag
from ui.ui_main import Ui_MainWindow


class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ui设置
        self.setAcceptDrops(True)
        self.ui.toolButton_add_tag.setIcon(QIcon(_ICON_ADD))
        self.ui.toolButton_delete_tag.setIcon(QIcon(_ICON_DELETE))
        self.ui.toolButton_restore_tag.setIcon(QIcon(_ICON_RESTORE))
        self.ui.toolButton_restore_tag_file.setIcon(QIcon(_ICON_RESTORE))
        self.ui.pushButton_confirm.setIcon(QIcon(_ICON_CONFIRM))
        self.ui.pushButton_clear.setIcon(QIcon(_ICON_CLEAR))
        self.ui.label_down.setPixmap(QPixmap(_ICON_DOWN))
        self.ui.label_down.setAlignment(Qt.AlignCenter)
        self.ui.label_filename_original.setStyleSheet('border: 1px solid black;')
        self.ui.label_filename_preview.setStyleSheet('border: 1px solid blue;')
        self.ui.comboBox_tags.addItems(_IDENTIFIER)

        # 绑定槽函数
        self.ui.toolButton_add_tag.clicked.connect(self.add_tag)
        self.ui.toolButton_delete_tag.clicked.connect(self.delete_tag)
        self.ui.toolButton_restore_tag.clicked.connect(self.restore_tag_state)
        self.ui.toolButton_restore_tag_file.clicked.connect(self.restore_tag_file_state)
        self.ui.pushButton_clear.clicked.connect(self.unchecked_all_tag)
        self.ui.pushButton_confirm.clicked.connect(self.rename)
        self.ui.comboBox_tags.currentIndexChanged.connect(lambda: self.drop_path(self.path))

        # 初始化
        self.filetype = None
        self.path = None
        self.parent_dirpath = None
        self.filetitle = None
        self.suffix = None
        self.ui.listWidget_tag.setEnabled(False)

        # 加载数据库中的tag
        self.load_tags_db()

    def drop_path(self, path):
        """拖入文件"""
        if not path:
            return
        self.path = path
        self.parent_dirpath, filename = os.path.split(path)
        if os.path.isdir(path):
            self.filetype = 'dir'
            self.filetitle = filename
            self.suffix = ''
        else:
            self.filetype = 'file'
            self.filetitle, self.suffix = os.path.splitext(filename)

        self.ui.label_filename_original.setText(self.filetitle)
        self.ui.label_filename_preview.setText(self.filetitle)
        self.show_file_tag()
        self.ui.listWidget_tag.setEnabled(True)

    def load_tags_db(self):
        """加载数据库中的tag"""
        self.ui.listWidget_tag.clear()
        tags = function_config.read_tags()
        file_tags = self.get_tags_in_widget(self.ui.listWidget_tag_file)
        for tag in tags:
            item = QListWidgetItem()
            checkbox = CheckBoxTag(tag)
            if tag in file_tags:
                checkbox.setChecked(True)
            checkbox.signal_state_changed.connect(self.tag_state_changed)
            self.ui.listWidget_tag.addItem(item)
            self.ui.listWidget_tag.setItemWidget(item, checkbox)

    def show_file_tag(self):
        """显示文件Tag"""
        tags = self.analyse_filename_tags()
        self.set_file_tags(tags)

    def set_file_tags(self, tags: list):
        """添加文件Tag到ui上"""
        self.ui.listWidget_tag_file.clear()
        for tag in tags:
            item = QListWidgetItem()
            checkbox = CheckBoxTag(tag)
            checkbox.signal_state_changed.connect(self.tag_state_changed)
            checkbox.setChecked(True)
            self.ui.listWidget_tag_file.addItem(item)
            self.ui.listWidget_tag_file.setItemWidget(item, checkbox)

    def add_tag(self):
        """添加tag"""
        dialog = QInputDialog()
        result = dialog.getText(self, '添加tag', '输入tag：')
        if result[1]:
            tag = result[0].strip()
            tag = function_normal.check_filename_feasible(tag, True)  # 替换非法字符
            if tag and tag not in function_config.read_tags():
                self.insert_tag(tag)
                function_config.inset_tag(tag)

    def delete_tag(self):
        """删除tag"""
        item_widget = self.ui.listWidget_tag.itemWidget(self.ui.listWidget_tag.currentItem())
        tag = item_widget.text()
        result = QMessageBox.question(self, '删除Tag', f'是否确认删除"{tag}"', QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            item_widget.setChecked(False)
            self.ui.listWidget_tag.takeItem(self.ui.listWidget_tag.currentRow())
            function_config.delete_tag(tag)

    def restore_tag_state(self):
        """还原tag勾选状态"""
        for i in range(self.ui.listWidget_tag.count()):
            item_line = self.ui.listWidget_tag.item(i)
            item_widget = self.ui.listWidget_tag.itemWidget(item_line)
            item_widget.setChecked(False)

    def restore_tag_file_state(self):
        """还原文件tag勾选状态"""
        for i in range(self.ui.listWidget_tag_file.count()):
            item_line = self.ui.listWidget_tag_file.item(i)
            item_widget = self.ui.listWidget_tag_file.itemWidget(item_line)
            item_widget.setChecked(True)

    def insert_tag(self, tag):
        """插入tag"""
        item = QListWidgetItem()
        checkbox = CheckBoxTag(tag)
        checkbox.signal_state_changed.connect(self.tag_state_changed)
        self.ui.listWidget_tag.addItem(item)
        self.ui.listWidget_tag.setItemWidget(item, checkbox)

    def tag_state_changed(self, tag, is_checked):
        """tag勾选框状态被修改"""
        self.connect_custom_and_file_tag(tag, is_checked)
        if self.path:
            new_filetitle = self.calc_new_filename()
            self.ui.label_filename_preview.setText(new_filetitle)

    def connect_custom_and_file_tag(self, tag, is_checked):
        """联动相同的自定义tag和文件tag的勾选状态"""
        self.set_tag_state(self.ui.listWidget_tag, tag, is_checked)
        self.set_tag_state(self.ui.listWidget_tag_file, tag, is_checked)

    def unchecked_all_tag(self):
        """所有tag变为不勾选状态"""
        self.set_tag_unchecked(self.ui.listWidget_tag)
        self.set_tag_unchecked(self.ui.listWidget_tag_file)

    def calc_new_filename(self):
        """计算新的文件名"""
        filename_old = self.filetitle
        identifier = self.ui.comboBox_tags.currentText()
        tags_layout = self.get_tags_in_widget(self.ui.listWidget_tag_file)
        tags_layout_file = self.get_tags_in_widget(self.ui.listWidget_tag)
        tags_selected = tags_layout[0] + tags_layout_file[0]  # 选中的tag
        tags_unselected = tags_layout[1] + tags_layout_file[1]  # 未选中的tag

        split_filename = filename_old.split(identifier)
        # 删除未选中的tag
        check_tags = [i.upper() for i in tags_unselected]
        for part in split_filename.copy()[1:]:  # 使用[1:]，防止出现分割后的第1个元素不含标识符但是和tag同名
            if part.strip().upper() in check_tags:
                split_filename.remove(part)
        # 添加选中的tag
        check_split = [i.strip().upper() for i in split_filename]
        for tag in tags_selected:
            if tag.upper() not in check_split:
                split_filename.append(tag)

        # 组合文件名
        new_filename = identifier.join(split_filename)

        return new_filename

    def rename(self):
        """执行改名"""
        # 检查重名文件名
        preview_filename = self.ui.label_filename_preview.text()
        no_dup_filename = preview_filename  # 该文件名不含后缀
        files_exists = [i.upper() for i in os.listdir(self.parent_dirpath)]
        count = 0
        while True:
            filename_with_suffix = no_dup_filename + self.suffix
            if filename_with_suffix.upper() in files_exists:
                count += 1
                no_dup_filename = preview_filename + f' - New{count}'
            else:
                break

        # 重命名
        result = QMessageBox.question(self, '重命名', f'是否重命名为"{no_dup_filename}"',
                                      QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            new_path = os.path.normpath(os.path.join(self.parent_dirpath, no_dup_filename + self.suffix))
            try:
                os.rename(self.path, new_path)
                self.reset_app()
            except OSError:  # 文件被占用时报错
                QMessageBox.warning(self, '失败', '文件/文件夹被占用，请关闭后重试')

    def analyse_filename_tags(self):
        """分析文件名，提取tag"""
        identifier = self.ui.comboBox_tags.currentText()
        filename = self.filetitle
        try:
            tags_analyse = filename.split(identifier)[1:]
        except IndexError:
            tags_analyse = []

        tags_analyse = [i.strip() for i in tags_analyse]
        return tags_analyse

    def reset_app(self):
        """重置程序"""
        self.filetype = None
        self.path = None
        self.parent_dirpath = None
        self.filetitle = None
        self.suffix = None

        self.ui.listWidget_tag.clear()
        self.ui.listWidget_tag_file.clear()
        self.ui.label_filename_original.clear()
        self.ui.label_filename_preview.clear()

        self.load_tags_db()
        self.ui.listWidget_tag.setEnabled(False)

    def get_tags_in_widget(self, list_widget):
        tags_selected = []
        tags_unselected = []
        for i in range(list_widget.count()):
            item_line = list_widget.item(i)
            item_widget = list_widget.itemWidget(item_line)
            tag = item_widget.text()
            is_checked = item_widget.isChecked()
            if is_checked:
                tags_selected.append(tag)
            else:
                tags_unselected.append(tag)

        return tags_selected, tags_unselected

    def set_tag_state(self, list_widget, tag, is_checked):
        """手动设置tag的勾选状态"""
        for i in range(list_widget.count()):
            item_line = list_widget.item(i)
            item_widget = list_widget.itemWidget(item_line)
            tag_item = item_widget.text()
            if tag_item == tag:
                item_widget.setChecked(is_checked)

    def set_tag_unchecked(self, list_widget):
        """手动设置控件中的所有tag为不勾选状态"""
        for i in range(list_widget.count()):
            item_line = list_widget.item(i)
            item_widget = list_widget.itemWidget(item_line)
            item_widget.setChecked(False)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            path = urls[0].toLocalFile()  # 获取首个路径
            self.drop_path(path)


def main():
    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    # 设置白色背景色
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(255, 255, 255))
    app.setPalette(palette)
    show_ui = Main()
    show_ui.show()
    show_ui.setWindowIcon(QIcon(_ICON_TAG))
    app.exec()


if __name__ == '__main__':
    function_config.create_default_pkl()
    main()
