import os
import re


def humanize_size(size: int) -> str:
    units = iter(("K", "M", "G", "T"))
    correct_size = str(size)
    while size >= 1024:
        size /= 1024
        try:
            correct_size = f"{size:.1f}{next(units)}"
        except StopIteration:
            correct_size = f"{size:.1f}"
    return correct_size


def la_to_lha(la_output_file) -> str:
    la_output_path = os.path.abspath(la_output_file)
    lha_output_path = os.path.abspath("lha_output.txt")
    size_pattern = (
        r"^"
        r"(?P<permissions>\S{10})"
        r"\s+(?P<links>\d+)"
        r"\s+(?P<owner>\S+)"
        r"\s+(?P<group>\S+)"
        r"\s+(?P<size>\d+)"
    )
    full_text = ""
    sizes = re.compile(size_pattern)
    with (
        open(la_output_path, "r", encoding="utf8") as la_output,
        open(lha_output_path, "w", encoding="utf8") as lha_output,
    ):
        for cur_line in la_output:
            search = sizes.search(cur_line)
            if search:
                wrong_size = int(search.group("size"))
                correct_size = humanize_size(wrong_size)
                start, end = search.span("size")
                new_line = cur_line[:start] + correct_size + cur_line[end:]
            else:
                if re.match(r"total", cur_line):
                    new_line = f"total {full_files_size(la_output_file)}\n"
                else:
                    new_line = cur_line
            full_text += new_line
            lha_output.write(new_line)
    return full_text


def full_files_size(la_output_file) -> str:
    la_output_path = os.path.abspath(la_output_file)
    size_pattern = (
        r"^"
        r"(?P<permissions>\S{10})"
        r"\s+(?P<links>\d+)"
        r"\s+(?P<owner>\S+)"
        r"\s+(?P<group>\S+)"
        r"\s+(?P<size>\d+)"
    )
    total_size = 0
    with open(la_output_path, "r", encoding="utf8") as la_output:
        for cur_line in la_output:
            sizes = re.compile(size_pattern)
            search = sizes.search(cur_line)
            if search:
                size = int(search.group("size"))
                total_size += size
    humanized_total_size = humanize_size(total_size)
    return humanized_total_size


def get_counts(la_output_file):
    la_output_path = os.path.abspath(la_output_file)
    permissions_pattern = (
        r"^"
        r"(?P<permissions>\S{10})"
    )
    files_count = 0
    dirs_count = 0
    symlinks_count = 0
    permissions = re.compile(permissions_pattern)
    with open(la_output_path, "r", encoding="utf8") as la_output:
        for cur_line in la_output:
            search = permissions.search(cur_line)
            if search:
                permission = search.group("permissions")
                if permission.startswith("d"):
                    dirs_count += 1
                elif permission.startswith("-"):
                    files_count += 1
                elif permission.startswith("l"):
                    symlinks_count += 1
    return {"dirs": dirs_count, "files": files_count, "symlinks": symlinks_count}


file = "output.txt"
la_to_lha(la_output_file=file)
print(get_counts(la_output_file=file))
