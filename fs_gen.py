# -*- encoding: utf-8 -*-

import argparse
import ctypes
import platform
import sys


class XYFSImageTool:

    def __init__(self, dll_path: str):
        if platform.system().lower() == 'windows':
            if sys.version_info.major >= 3 and sys.version_info.minor >= 8:
                dll = ctypes.CDLL(dll_path, winmode=0)
            else:
                dll = ctypes.CDLL(dll_path)
        elif platform.system().lower() == 'linux':
            dll = ctypes.cdll.LoadLibrary(dll_path)
        else:
            dll = None
            return

        dll.XYFSImageGenerator_new.argtypes = [
            ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_bool]
        dll.XYFSImageGenerator_new.restype = ctypes.c_void_p

        dll.XYFSImageGenerator_generate.argtypes = [ctypes.c_void_p]
        dll.XYFSImageGenerator_generate.restype = ctypes.c_int

        dll.XYFSImageGenerator_delete.argtypes = [ctypes.c_void_p]

        self.dll = dll

    def generate(self, src: str, dst: str, fs_image_size: int, reverse: bool, fs_type: str):
        if not self.dll:
            return False
        image_generator_c = self.dll.XYFSImageGenerator_new(ctypes.c_char_p(src.encode('utf-8')), ctypes.c_char_p(
            dst.encode('utf-8')), ctypes.c_int(fs_image_size), ctypes.c_bool(reverse), ctypes.c_char_p(fs_type.encode('utf-8')))
        ret = self.dll.XYFSImageGenerator_generate(image_generator_c)
        self.dll.XYFSImageGenerator_delete(image_generator_c)
        return False if ret < 0 else True


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', help='filesystem type', type=str,
                        required=False, default='littlefs', choices=['littlefs'])

    parser.add_argument(
        '-r', help='restore files and directories from binary to dest directory with specified filesystem type', action='store_true')

    parser.add_argument(
        '-s', help='source folder or source bin', type=str, required=True)

    parser.add_argument(
        '-d', help='dest bin path or dest folder', type=str, required=True)
    
    parser.add_argument(
        "-b", help='dll or so path', type=str, required=True)

    parser.add_argument('-i', help='image size in byte',
                        type=int, required=False, default=48*1024)

    args = parser.parse_args()

    # TODO: check if src and dst meet the requirements
    image_tool = XYFSImageTool(args.b)
    ret = image_tool.generate(args.s, args.d, args.i, args.r, args.t)
    if not ret:
        sys.exit(-1)


if __name__ == '__main__':
    main()
