import os
from pathlib import Path
from gooey import Gooey, GooeyParser

#TODO: Add confirmation screen with list of changes to be made

@Gooey
def parse_args():
    parser = GooeyParser(description='rename selected files sequentially based on date-modified value')
    parser.add_argument('files', help='files to rename', widget="MultiFileChooser")
    return parser.parse_args()


def main():
    parsed_args = parse_args()
    fileList = dict.fromkeys(str(parsed_args.files).split(';'), 0)
    for k, v in fileList.items():
        fileList[k] = int(os.path.getmtime(k))
    {k: v for k, v in sorted(fileList.items(), key=lambda item: item[1], reverse=True)}
    i = 1
    for k, v in (fileList.items()):
        parent = Path(k).parent
        os.rename(k, ''.join([str(parent), '/', 'GH', str(i), '.mp4']))
        i += 1


if __name__ == "__main__":
    main()
