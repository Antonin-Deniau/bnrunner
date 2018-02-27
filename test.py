import bnrunner, import_test
from binaryninja import HighlightStandardColor

def main(): 
	block = bv.get_basic_blocks_at(0x8670)[0]
	block.highlight = HighlightStandardColor.BlueHighlightColor
	print(bv)

bnrunner.run_from_path() if __name__ == '__main__' else main()