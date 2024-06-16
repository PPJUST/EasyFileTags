from typing import Union


def check_filename_feasible(filename: str, replace: bool = False) -> Union[str, bool]:
    """检查一个文件名是否符合Windows文件命名规范
    :param filename: str，仅文件名（不含路径）
    :param replace: bool，是否替换非法字符"""
    # 官方文档：文件和文件夹不能命名为“.”或“..”，也不能包含以下任何字符: \ / : * ? " < > |
    except_word = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
    if not replace:  # 不替换时，仅检查
        # 检查.
        if filename[0] == '.':
            return False

        # 检查其余符号
        for key in except_word:
            if key in filename:
                return False
        return True

    else:
        for word in except_word:  # 替换符号
            filename = filename.replace(word, '')
        while filename[0] == '.':  # 替换.
            filename = filename[1:]

        return filename.strip()
