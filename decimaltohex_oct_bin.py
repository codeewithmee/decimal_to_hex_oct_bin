import pyfiglet
from argparse import ArgumentParser

parser = ArgumentParser(description="Convert Decimal to hex , oct and bin using python",epilog="""This is a description usage
    python decimaltohex_oct_bin.py -n A -b 16""")

req_parser = parser.add_argument_group('Required Argument')

req_parser.add_argument('-d','--decimal',dest='decimal',type=int,help="specify decimal number",required=True)

args= parser.parse_args()
decimal = args.decimal

class Dec_to_hex_oct_bin(object):
	"""docstring for Dec_to_hex_oct_bin"""
	def __init__(self,decimal):
		self.decimal = decimal
		self.Banner("Dec to h_o_b")

	def Banner(self,name):
		banner = pyfiglet.figlet_format(name)
		print(banner)

	def dec_to_hex_oct_bin_converter(self,decimal):
		x=hex(decimal)
		y=oct(decimal)
		z=bin(decimal)
		return x,y,z

	def main(self):
		x,y,z = self.dec_to_hex_oct_bin_converter(self.decimal)
		print(f"Hexadecimal is {x}")
		print(f"Octal is {y}")
		print(f"Binary is {z}")

if __name__ == '__main__':
	res = Dec_to_hex_oct_bin(decimal)
	res.main()
