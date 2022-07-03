#pylint:disable=W1309
#pylint:disable=W0612
#pylint:disable=W0611
import os, sys
from pyaxmlparser import APK
from glob import glob
from zipfile import ZipFile as zf

# const variabel
TEMPDIR = "/storage/emulated/0/.temp/apk_installer"
DATADIR = "/data/app"

# fungsi utilitas
def execute(perintah, su=True):
	if su:
		os.system(f"su -c {perintah}")
	else: os.system(perintah)
def executes(perintah, su=True):
	if su:
		ret_val = os.popen(f"su -c {perintah}").read()
		if not bool(ret_val):
			return 0
		else: return ret_val
	else:
		ret_val = os.popen(f"su -c {perintah}").read()
		if not bool(ret_val):
			return 0
		else: return ret_val
###-+-+-+-+-+-####
def echo(text):
	print(f"-- {text}")
def clear_temp():
	execute(f"rm -rf {TEMPDIR}/*")


def main():
	execute("clear")
	if bool(sys.argv[1]) and sys.argv[1] == "--apks":
		is_apks = True
	else: is_apks = False
	
	if is_apks:
		# extrak split file
		if os.path.exists(sys.argv[2]):
			apks_file = str(sys.argv[2])
		else: print("error apks file not found")
		echo("extract base and split apk")
		with zf(sys.argv[2], 'r') as xyz:
			xyz.extractall(f"{TEMPDIR}")
		apk = APK(f"{TEMPDIR}/base.apk")
		apk_package = f"{apk.package}-1"
		list_split = glob(f"{TEMPDIR}/split_*")
		echo('installing base apk')
		execute(f"pm install -r {TEMPDIR}/base.apk > /dev/null")
		echo("installing split apk")
		for i in range(0, len(list_split), 1):
			split_apk = list_split[i]
			execute(f"busybox cp -v {split_apk} {DATADIR}/{apk_package}")
		echo("set split apk permision")
		execute(f"chmod 644 {DATADIR}/{apk_package}/split_*apk")
		if executes(f"[ -d {DATADIR}/{apk_package}/lib/arm ] && echo $? || echo $?"):
			execute(f"mkdir -p {DATADIR}/{apk_package}/lib/arm")
			#lib_dir = f"{DATADIR}/{apk_package}/lib/arm"
		# check library
		for i in range(0, len(list_split), 1):
			with zf(list_split[i], 'r') as xyz:
				list_file = xyz.namelist()
			if 'lib/' in list_file[i]:
				lib = list_split[i]
				execute(f"unzip {TEMPDIR}/{lib} lib/*so -d {TEMPDIR}")
				break
		execute(f"busybox mv -v {TEMPDIR}/lib/*/*so {DATADIR}/{apk_package}/lib/arm/")
		echo("set library permision")
		execute(f"chmod 755 {DATADIR}/{apk_package}/lib/arm/*so")
		echo("installation finish")
		clear_temp()
###+-+-+-+-+####
if __name__ == '__main__':
	main()