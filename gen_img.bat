python gen_files1.py
pause
python fs_gen.py -s temp -b fs_gen_x64.dll -d littlefs.bin -i 36864
pause
python xy_packer.py . littlefs.ini
pause