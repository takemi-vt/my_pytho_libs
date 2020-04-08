import sys

#CUIのエスケープシーケンス制御の簡易クラス
class Cui():
	#画面のクリア
	@staticmethod
	def cls():
		sys.stdout.write("\033[;H\033[2J")

	#num行上に上がり、カーソル位置を行頭
	@staticmethod
	def lineUp( num ):
		sys.stdout.write("\033[" + str(num) + "F" )

	#num行上に下がり、カーソル位置を行頭
	@staticmethod
	def lineDown( num ):
		sys.stdout.write("\033[" + str(num) + "E" )

	#カーソル行を削除(mode=0:カーソルより後ろを削除/mode=1:カーソルより前を削除/mode=2行全体を削除)
	@staticmethod
	def lineCls( mode = 0):
		sys.stdout.write("\033[" + str(num) + "K" )

	#カーソルを左にnum文字移動
	@staticmethod
	def left( num ):
		sys.stdout.write("\033[" + str(num) + "D" )

	#カーソルを右にnum文字移動
	@staticmethod
	def right( num ):
		sys.stdout.write("\033[" + str(num) + "C" )

	#色付き文字を表示
	@staticmethod
	def strColor( caption, cl ):
		cl = cl.lower()
		code = "\033["
		if( cl == "black" ) :
			code += "0;30m"
		elif( cl == "blue" ) :
			code += "0;34m"
		elif( cl == "green" ) :
			code += "0;33m"
		elif( cl == "cyan" ) :
			code += "0;36m"
		elif( cl == "red" ) :
			code += "0;31m"
		elif( cl == "purple" ) :
			code += "0;35m"
		elif( cl == "brown" ) :
			code += "0;33m"
		elif( cl == "light-gray" ) :
			code += "0;37m"
		elif( cl == "dark-gray" ) :
			code += "1;30m"
		elif( cl == "light-blue" ) :
			code += "1;34m"
		elif( cl == "light-green" ) :
			code += "1;32m"
		elif( cl == "light-cyan" ) :
			code += "1;36m"
		elif( cl == "light-red" ) :
			code += "1;31m"

		sys.stdout.write( code + caption + "\033[0m" )

	#色付き(色をRGBで指定)文字を表示
	@staticmethod
	def strRGB( caption, r, g, b ):
		sys.stdout.write( "\033[38;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m" + caption + "\033[0m" )
	
	#カーソルをx,yの位置へ移動させる
	def locate( x, y )
		sys.stdout.write( "\033[38;2;" + str(y) + ";" + str(x)+ "H" )

# text Code
#インクルードして使うときは下記行を削除
Cui.cls()
print("foo")
Cui.lineDown(2)
Cui.strColor( "bar", "light-cyan" )
print("")
Cui.strRGB( "foobar", 200, 10, 200 )
print("")