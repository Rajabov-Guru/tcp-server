import struct
import tempfile

import cv2
from h26x_extractor.h26x_parser import H26xParser

other = (b"\x00\x00\x00\x01\x13[%\xb8 "
         b'\x03\xbf\xff\xfe\x1e\x12(\x00\x08\x08\xfb\xef\xbe\xfb\xef\xbe\xfb\xef\xbe\xfb\xef\xbe\xfb\xef\xbe\xfb\xef'
         b'\xbe\xfb\xef\xbe\xfb\xef\xbe\xfb\xef\xbe\xfb\xef\xbe\xfb\xef\xbe\xfa\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
         b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
         b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
         b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
         b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
         b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
         b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
         b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
         b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
         b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
         b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
         b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
         b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
         b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
         b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
         b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
         b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
         b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
         b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
         b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
         b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
         b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
         b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
         b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
         b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
         b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
         b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
         b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
         b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
         b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
         b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
         b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xb3b\xeb\xae\xba\xeb\xae'
         b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xff\xff\xe3\x04<\x98\xbf\xff\xe1\x04\x1d\xeb\xad_|\xbd\xf7\xdf'
         b'}\xf7\xdf}\xf7\xdf}u\x98\x82\\k \x86l\xf4\xff\xfa\xd9\xae\xba\xff\xe3\xf8\x04)\xc4\xf3\xac\'\x8b\xfe\xd6'
         b'\x9e\x9a}\xfc\x7f\xe1\xd0\x9f]\x9f\xa9\xd4;\x962Z\x98\x88L\x90F\xd4\x8d\xff\xea\xfb\xda\x8fxz\xaf\xe9\xa7'
         b'\xfe=W\xa5\xa4\x97\xfbUk\x1e\xaa].\xe5\xd2\xef\xfe\xd6\xd5G\xaa\xfbm\xff\xedU\xac\xea\x95Z\xa0c\xd4\x94'
         b'\xfb\x7f\xfbX\xf5%\xfd\xaf\xfd\xa9H-m]\xa9,'
         b'z\x94\x83O6\x9b\x7f\xf6\xae\xd6\xd4g\xc3\xd4\xa4\x1f\xa7\xff\xb5\xb5v\xaeu\x19\xf7Z\x88H?\x14\x87\xfc\x14'
         b'\xd7\xee\xf1S\xd7\x1f\x94\x8f\xfbm\xfe\xb1Z\xeb&.\xbf\xf4\xfbP!K~\xd7\xf8\x96P\xf6_I~\x96\xa15\x17\xff\xf6'
         b'\xfb\xce\xa1\x939V\xa4\xc6\xa6\xa3UjL:\xadG\xa9I\x7f]$\xb4\x92\x1e\xa4%\xfa\xff\xf9\xfc\x7f\xa0\xb7o\xd3'
         b'~\xa1\xf1\x0f\x00 \xd8\x87/\xe3t^Z\x1b=v\xff\xff\xc0\x044\x0bu\xba\xf6\xfcz\x84\x0e7a\x9b\xf9w\xff\x87\xf0'
         b'\x08\x85\x02\x1a\xed\x04\xd4m\xb0\xd5%V\xfa\xffk+P\x1diK5\x84\xd5/\xffi\xae\xa3\xd5\xff\xd3OM=\xab\xb5\x7f'
         b'\xf8\xff@\x82\\\xed\\\xeaZu\xa9\xc8\'w\xe8\xf5-?\xd2\xe9%\xb5`\xda\xbbW\x1e\xa5\xa7\xff\xa4\x96\xd4}\x90O'
         b'\x7f\xff\xb7\xf7\xfe1\xfa\x0b_\xc5\x7f\x7f('
         b'yr\x07\xb7\xd3\xff\xfc>\x088\xbcw\xfe\x9f\xdb\xc2\x19\x086\xff\xff]u\xd7\x1d\x83\xdf\xff\xf5\xad\xba\x8c'
         b'\xfa\xde\xff\xe0+\xd2\x1a\x13\x1d\xb5^\xb1.r\xaak\xf3<s\x1d\xf8\n\xaf\xfd\x82\xbc\xd9R5S_\x99\xe3\x98\xef'
         b'\xb2\n\xd8&p{X\xf2\xa5\xd55\'\x85\xa6O\xacr\x16p\x9d\xc3\xaa?\xf4\xbe7\x1d\xef\xf6\xb6\xb6\xae\xd6u\xd5'
         b'\xad\xad\xab\x91h\x9a[X\x8f\xd6\xb1\x0b\xe9\x16\xd6e\xfa\xd6\xd6\xb9\x97V\xb6\xb4\xf7\xd3\xaaz{'
         b'\xd4v\x1d\x9f\x1fu\xfc\xbc\x9f\x1d\x90`\xff\xa7o\xefu\xd7\\w\xff\xfe\xe9\xe9\xfag\xff\xe0\xab\xbe\xdf\xe9'
         b'\xf9\xe0\x1f\xfa\x05^\xdb\xfd<.\xa1\x16\x9e\xd1\xcb\x05\xfd\xb6\xff\xfe\xb6\xdfO6\xb7\xb5\xb5\xb5\x91o\xbe'
         b'\xbb\xe4\xe4\xe4\xef\x93\xa7\xa2m\xe6\xed]=u\xd2\xd2\xd2\xd15\x8e\xa6S\xcaJi\xeb\xff\xffG\x858\x9f/j\xd2p'
         b'\x86\xcf\xff\xdb\xef)\x05u\xd7\x1f\xfe\xff\xfaz\xe6u\xbd\xbc\xea\xb7\xb5\xac\xe4N\xfa\xa5V\xb4\xa9\x84'
         b'\x94pI\xff\x9f\xd3\xe9\xa6T\x8fr\xdf\xff\xf6\xc7\xff\xf6\xe9\xa7\xd3\x1f\xb3\xffm\xbd\xb6\xf7\xb4\xf3'
         b'\xd0vm\xff\xb6\x9a~\xba\xeb\xb7\xb7\xb2dVl\x9b['
         b'%\xc2k\xff\xd3OM>\xb2b\xd6\xba\x7f\x16\xbe\xf4\xff\xff\x89\xe2\x88\x16\xf8o\xcb\xdb\xf4\xea\x9e\x9e\x9e'
         b'\xb8C\x01#n{\xbf\xfd\xabp\xa6B_\xf4\xed\xfb\xc2\x04\xf6\xff\xfe\xba\xeb\xae\x9d\xb4\xb4\xea\xdf\xe08t\xc0'
         b'\x11\xb0\xdf\xbfw\xb4\x94\xbd\xd4C\xf0\x0f\x85\xf5\xb1\xbd\xfa\xfc\x7fM\x01\x8e\xcd\xe8k\xf4\x99\x8cf\xaf'
         b'\xf9\xff\xc3\xec\x15\xf5\xab\xdf\xe4\xef\x85\xb1\xa4\xcf\xff\xd6jKZ\xfe\'\xf1\xfe\xb2\xe6=\xee+\xf2\xfa'
         b'\xc6(sM?\xfap\xfc\x02\x9f\x9b\xf2\x18\xef\xd8\xda\x1e\xa8\xb93.\x1a_\xa6\x9c\x7f\xfdt\x13\xe2\xee\xd7\n'
         b'\xa8\xd1\xb2\x9f\xa34m\xa6\x9f\xf4"\xa1\xf6\t\xa5M$\xff\xf1kjI~\xd6\x13['
         b'}\xb6\xff\xf3\xa5\xacZ\xb4\xad\xb7\xf8\xb5\xabM~\xd6E\x14mmmmmmmx\x7f\xf6\x00#\xf9x\xad\xfd\x8e\xaf\xcd'
         b'\xe5+\xd3\xd3\xd7\xf9O\xfbc)B\xff|\xde\x1b\xc5\x1e\xed\x7f\xe9\xf4\xe3\x9d\xaf\xf6\xfb}u\xd7\\q#\xe9\x87'
         b'\xbf\xff\xd3\xca\xech\x99\xd6\xf6\xaauZ\xbegW\xb5\xff\x87\xc6l)\x97\xfc\xbc{\x92>\xaeMM['
         b'\xed7i\xac~\x12\xe2u\xb6Mf\xda\xdd-\xbd$\xa3\xf0\xec\xccM\xff\xb6\xdbI\xdb\xdf\xfe\xa0=o\xf2\xdc\xd4^\x94'
         b'\xccw| \x1c\xfc\x8e\xd39\xcd\xfc7\xef6G\xb9H4['
         b'&?M=4\xc2\x0e\x01\xfdWu\r\x93\x7fO\xf8\xfd\xdd\xad6\xbf\xf0\x8eJ&1\xdf\xff\xe4\xd5\xf7\xdf]u\xd7]u\xd7\xff'
         b'\xf2\xf6+b\x93\x99\x9fN\xf5\xd3\xca\xe8i\xeb\x84?\xffG\xe3\xdc\x84\x16\xdb\xff\xe9\xdb\x1c\xe4\x1f\xffO'
         b'\xfa\xeb\xae\xbas\xf4\xf0\xb1,_\xff\xdb\xbf\x7f\xff\xf7]d\x04\x1da\'_\xff\xb6ZGQ\xca\xbf\xfa\xff\xff\xf1'
         b'\x0c\x10\xc3~\xf1\xdf\x7f\xe8\x07\xe4\x04\x1e\x03\xa7S\xfa\x8a\xd5k\xf8A\xc1\x8c\x16\x93\xb6\xdd6\xd1\x13v'
         b'\x9a\xcd\xb1\xf8\x08\x9b\x98\x1f#l{\xad\xdbvjn\x87sh\xfcD\x8ai\xa2\xa6\x9d\xa4\xb1z]0\x0e\xff '
         b'\xbf\x13\xa5\xaaTu\x1e\xa0\xff\xa1q\xde\x997-\xeb\xb5\xfb\xbf\x88\xbf\xd8"\xf6i\xb4\x9d\xf5\xd7]u\xd7]u'
         b'\xd7]u\xc2N8\x99\xff,%\x85\x15\x16\xa2v\xcbR\xd3\xbaz\xe3\xb0\xf9\x87\x13V\xd9:n\xfc\xc8\xa9\xf4\xe3\xc9'
         b'\x7f\xff\xd3Lvm\xff\xd3\xe9\xd7]u\xc79\xfd\xef\xff\xe9\x7f\xb7\xf3\xc8\x08\xf6\xf7\xed\x87\xf6\xec/K\xae'
         b'\xe7\xbf\xa9\x8f\xfb\x0cE\xfc\xd4\xcbp\'8 '
         b'\x00+1\xd0\xd8\xb9\xa4\x8dW\xb2\xfb\x1f5>\xcb\xcd\xdf\xff\xff\xf11a\xcd\x00\xa6e\ry\xda\xff\x04\xc3\x80'
         b'\xff\x0b\xdf\x87k\xb7\xc6l}#]:\xb5\xc0?\xffa{'
         b'\xfd;N\xbe\xb5\xb5\xb5\xbe\xbf\xff\xf8A\x0e\t\x1e\xed\xaf\xfe\xbf\xe0\x82\xaa7\x83\xae\xba\xeb\xae\xba\xeb'
         b'\xae\xba\xeb\xc3\xff\xfbs~V:\xdb\xe7\xf4M-\x12\xdax\xef\xff\xf7\xc2\x18\xe8\xad\x8a\xbav\xf5\xf6\xb6\xe7'
         b'\xc1\xfa?\xffI&\xeb\xae\xba\xe8\x947\xccKz\x93\x99\xfa\x88SeD\xad\xe7^T\xf4\xf3w\xff\xff\xd8+\xa1\xd6\xba'
         b'\xfd=u\xd7]\x7f\xcf\xff\x92_\xff\xe1\xea\xf5\xd7]u\xd7]u\xd7]\x7f\xff\xb7a;\x1f3\x1d\x13]\x12\xe9\xeb\x8e'
         b'\xf4\xfa\x7f\xfb{\xeb\xae\xba\xe3\xb2\xb1\xfb\xfd\xfay\x9e\xcf\xfe!\x9e\xc1$\xddr\xac\x99\xf5)#\x90\xa2'
         b'\x1fU\xdb\xcc\xf7\xad\x7f\xff\xec73=|\xef\xbd\xe9\xeb\xae\xba\xeb\xae\xfa\xeb\xae\xba\xeb\xae\xba\xeb\xae'
         b'\xbf\xff\xfd\x85\xe9\xd4\xcc\xb1Zw\xa7Mu\xb1\'\xae\xfb{'
         b'\xeb\xae\xba\xeb/O\x15\x99u\xbd\xff\x8f\xe1\x80lO\x1c\x84\xf5\xfd\xc2\x0f\xfe\xcb\xfc('
         b'\xa1\xe4\xf1\x9b\xb2\xff\xffS\xd7ON\xab\xff\xff\xd8_\xad\xbe\xf5\xd7]u\xd7]u\xd7]u\xd7]u\xd7]~\xdfh}\x85'
         b'\xf2\xff\xa1\xd4\xce\xc7\xd4K\x90\x91F\x95R\xd2\xd7]u\xd7\\r\x97\xff\x7f\xbe\x9e\x9ew\xe7\xa7\xbe\x9e'
         b'\xbazz\xff\xf4\xfe\xc22U\xd7]u\xd7]u\xd7]u\xd7]u\xd7_\xfc?\xe1L\xac\xcc\xa2\xdf\xff\xffa=\xfa\x1d\xd3\xd3'
         b'\xd15\xff\x8f\xfe\x1e\xf2g\x9f\xff\xc3\xdd\x9aC\xb3Sk\xff\xeb\xae\xba\xeb\xbe\x9eO\xff\xf6Eu\xdf\xb8o\xca'
         b'\xe6\x97\x1f\xdb%C\xa5\x16\xc1:\xd6\xed;q\x13\xfe<1\xfb}>\xbc\xece\xbf['
         b'/mj\x111\xdd\xac\xd9sQ\x85;\xb1\xa2\x8ef['
         b'i\x8fz|%\xf2\x11===k\xff\xff`\x8bNF\x13\xd7]u\xd7]u\xd7]u\xd7]u\xd7]\x7f\xff\xfc)\x91G\xcc\xc7\xff\xfd\x87'
         b'\xbc\xfd:i\xca\xba\xeb\xa7W\xa0o\xbd\xb5\xd7]u\xc78}L\xff{\xfd,'
         b'0\xa2\xff_\xfe9\x8c\x15o\xa7\x8b\xc4\xfa\xb7\xd3\xe3\xc9@\xe9\xff\xffnn\x9e\x9dS\xd7\xff\xff\xb0\xbf\x93'
         b'\xd8\xf2U\xd7]u\xd7]u\xd7]u\xd7]u\xd7_\xff\xff\n{'
         b'\x1f\\\xbf\xff`\x83\x99\x9azr\xf4\xf1\xd9\xa9\xdb\xef\xf7\xd3\x8c5|w\xf6\xff\xfb\xd2]u\xd7^\x98\x7f\xf9'
         b'\x08\x9eg\xd4\xce\xb1\x7f\xfc\x07\xa0\xee('
         b'\xfej\x00\x89\x96\xbd\xff\xfc\x00<\x16\xe5d\xd9\x80\x7f\xa7\xf4\xf4\xf3?\xa8\x9f\xff\xfd\x85\xfd\x8e\xb6'
         b'\xddO]u\xd7]u\xd7]u\xd7]u\xd7]\x7f\xff\xf6\x87\xfd?\xff\xfb\x0b\xdf\xa7|\xa9\xd5+\xaf\xea\x93\xfe\x18O'
         b'\x12i\xf1t\xf5\xd7}u\xd7]q\xcf\xff\xef\xe9\xe3\x89\t\x9c\xf5\xfbk\xf5\xf9\xf5\xcb\xf8O\xd2k\xfa\xab\xc7'
         b'\xff\xd0\xe5E\x8d\x9dC\xee\x9b\xad\x9f\x95\x7f\xd3\x7f\xff\x82\xbd>\x13\xb7\xf2r=\xbc\x8b\xff\xd3\xc4 '
         b'\xbb\x9b=\xed\xf4\xce\xb8\xadc\xd4\xd9\xff\xd3\xd3L&\xbf\xf6\xdb\xdbo2\xedF\x9a\x1a\xb4\xd6u)#$Z\x94\x92'
         b'\xfflz\xff\xe9\xe9\xa7\x8bT\x97\xa7\xedOF\xa9\x1dR\x8eE\xab\xabm\xfeuI\xa7\\V\xb6\xa9~\x9f\xfa\x0f\xe3\x9f'
         b'\xf6\xff\xff\x0fh\xf9\x1dW_\x1f:\x7f\x83\x0e\xb4\xf9+t\xfe\x9e\xba\xeb\xae\xba\xebU\xca\xe5R\x9e\x9e\x89'
         b'\xb5\xa2imk\xb2dZZ[Y\x16E\x99mJ\xe9f['
         b'R\xba\xdd;\x9bv\xa7u\xb9\x9d\xfa\xc9\xb5s\xaf\xa9]\x933\xfaW\xae;No\xff\xfaz\xeb\xae\xba\xeb\xae\xba\xdd'
         b'\xbf\xff\xf8\xc8\x1d\xf7\xa4\xf8\xbd>\xdf\xfcy\xda\x81.\xd0\xab\xb9\t\xe3m\x7f\xf4\xffS\xa8\xbcS\x924\xc9'
         b'\xc8\xf5\x0b\xfd\xffk\xff\xf8\xffA]/\x8a\xc2jl\xff\x9bQ\xd2Wt\xca\x9f\xe3\x87\xc5?e\x9e\x94\x84\xd9\x968'
         b'\xf2\xff\xf8\x1a\x87\xa0Q\xefT\xa6I&\xff\xfb\x87A~\x8e\x0cW\xb6\xe7\xbf\xf8k\xd7\xdfG\x03\x16\xb9\xd7g\xb8'
         b'\xbb]\xecV\x9f\xff\xfe3\xb2\x0e\xe0c\xae\xfd)\x94}\xb6\xff\xff\xcd\x19\x1b\x9f=\x98\x93\xe2J1Chz\x8a\xff'
         b'\xb7\xff\xc7\xe3\xf9\xa1[\xf2\xe7\x0f\x95m('
         b'\xe3\x84\xc1\xfe\x8b\xcd\x1fW|+\x1e\x1f\xc0=\x02\xfe\xf0\xf0U\xa3\xe7d\xf7\xff\xe9\xc0\x1bB-\xdb5u\x89\xd0'
         b'\xbf\xbe;\x89\xd4K\x83\xba\x13W\xf6\xdb\xff\xfa\xd6\xd6\xd6\xd5\x9bXL\x9f\xe9\xff\xfa\xd6\xd6U\xbc\x98E'
         b'\x0c\x0f%\x90\x9a\xff\xfa\x9b\xfc\x10C~\xfb\xeb\xae\xb5}u\xff\xff\xf2=!\xea\x11a\\\xfcW\xff\xe1\xff\x98h'
         b'-\xc9w\xbe<z\x89\x12\x0f\xff\xb6\xde=Lm.\xfa\x7fk\xe3\xff\xf4\x12\xec\xd0>\x97\xfc8t\x12\xef\xd8?\xdb\xff'
         b'\xa0\x97.n\x8d\xffo\xfd\x05\xa7\x97S\xcf\xe8\xce\xaf\x85k\xfe\x82W\xa3\xf7\xb5>5\xcc7\xff\xe4\te\xa7\x13'
         b'\xed]\xf1\xea\x97\x9bS\xff\xce\xa4$\xf6\xf1\xea?\xeb{'
         b'm\xff\xedX6\xb2=\xf7\xdf]t\xb4\xb4\xb4\xb4\xb4\xb4\xb6\xb6\xb6\xb6M\xf5\xdf}\xf5\xda\xda\xda\xda\xda\xda'
         b'\xda\xd14\xb5\xd7]w\xdfk]--\xad--u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]=u\xd7]u\xd7]u\xd7]u\xd7'
         b']u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u'
         b'\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7'
         b']u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u'
         b'\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7'
         b']u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u'
         b'\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7'
         b']u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]\x7f\xffMpA\xa77_\xff\xc7L+\xdb\x17\xd1W_\xf3?\xd7\x87\xe6\xff\xc7\t'
         b'\x97\xf0\xbfj\x97zx\xee\xdd\x7f\xfe;\xfb\xaf\xfe\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
         b'\xae\xba\xeb\xae\xba\xff\xff\xf8W\xc5\xf4\xeb\xff\xeen\x1e\t&\xc9\xbah\xae\x9f\xeb\xe1R\xf8_\x9b"\xe9\xa5O'
         b'\xff\xfc\xf8\x7f\xc5\xf8\x87\xb4?\x0ft\xff\xeb\xff\x0f\xe2\xfa\xfa\xff\xff"\xef\xae\xba\xedk\xae\xba\xeb'
         b'\xe8i\xf4\x9a\xe9\x053g\xd6\xf4\xf5\xd7]u\xd7]u\xd7\\w\xeb\xff\xeb\xae\xba\xeb5\x17['
         b'\ru\xd7\xd3o\xff\x0fik\xb5\xae\xd6\xfb\xeb\xae\xfa\xeb\xae\xba\xff\x9a\xfe|?^\xba\xeb\xae\xbb_\xfe\x88\x9f'
         b'\x04\x916+Et\xf5\xd7]u\xd7]u\xd7]u\xd7]u\xdf]u\xd7]q\xdf\xff\xaf\xae;\xff\xd7\xf5\xd7]u\xd7]u\xd7\xfe\x1aQ'
         b'<\x14\xfa\xebx\xe7\xff\xffo\xff\xaf\x8c\x10\xf1\x06\x0f\xff\xfe\x90]\xd2\xa5_\xa7\xff\xf5W\xd0W\x0f\x95'
         b'>\xd5\x7f\xe2\xf4Y\xe1_H\x9b\xf3I\x9e~\xab\xc7k\xdf\xee\x9dz\x97\xe9\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
         b'\xeb\xae\xba\xeb\xae\xba\xeb\xae;\xd9\x7f\xfe\xbb\xeb\xae\xba\xeb\xae;\xff\xeb\xf5\xd7]u\xfek_\xf8\x7f'
         b'\\&\xa3\xc7:f\xdaf\xd6S\xfd:\xb7U\xff\xc8O\x97\xff\x82\xaa\xfb|\xebk['
         b'_\xa6\x9aN\x08h~\x1e\xf3e\xf5\xdb\xe9W\xea\xe9\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
         b'\xeb\xff\xff\x84\x10\xedL\xca\xe3\xbf\xff\xdf\\w\xfe\xff\xeb\xae\xba\xe3\xfa\xff\xff]u\xd7]\xad---u\xd7'
         b'\xf9\xeb\xff\x05U\xfb|\xea\x1f\xff\x05\xb7\xeb\xef\xd3\xd7]u\xd7]u\xd7]u\xff\xf0_\xc1\x047\xef\xae\xba\xeb'
         b'\xae\xba\xef\xae\xba\xeb\xae\xba\xeb\xae;\xff\xfe\xca\xba\xeb\xae\xba\xeb\xaf\xff\xe7\xf0A\xcd\xeb\xae\xd6'
         b'\xb6\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7\\w\xff\xfe\xeb\xae;\xff\xbf\xf5\xd7]u\xdf]u\xd7]u\xd7\xa7I\x7f\xe1'
         b'\xefIu\xd7}i.\xba\xeb\xae\xba\xeb\xae\xba\xeb\x8e\xff\xff\xd5u\xff\xfb~\x08&c\xae;\xf7\xff\xf5\xc7\x7f\x7f'
         b'\xfe\xbb\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xfa\xeb\xae\xba\xeb\xae\xba'
         b'\xeb\xae\xbb\xeb\xae\xfa\xeb\xae\xba\xeb\xae\xba\xe3\xbf\xffe\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
         b'\xba\xeb\xff\xff\xe0\x83\xd5\xf5\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xdf]u\xd7]u\xd7]u\xd7]j\xbe&\xb9\xe3'
         b'\xaf\x83\x08J\x92W\xef\xa0\xa1\xfd;w\x18%\xb7\xfe\x08\xb7\x93Q\xa9d\xda\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7'
         b']u\xd7]u\xd7]f\xc5\xff\xff^\x1f\xf1~?8\xfe\x18\xda\xe5\xcd\x1d\x8e{\x7f\xff\xd7Xc,'
         b'\xba\xef\xae\x96\x96\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb6.\xb9'
         b'\xb2c\xd3\xd7}u\xd2\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7['
         b'5\xd7]u\xdf]t\xb5\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7_\xff\xc7<\x10seu\xd6l]u\xd7]u\xd7}u\xd7]u\xd7]u\xd7]u'
         b'\xd7]u\xd7]u\xd7]u\xd7]u\xff\xff^\x1f\xcd\x9d\xc7\xe8>\xfc\x11z\xa3U\x02/\x8f\xf8{'
         b'\xbd=w\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd2\xd2\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u'
         b'\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7'
         b']u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u'
         b'\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7'
         b']u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u'
         b'\xd7]u\xd7]u\xd7^')
byte_string = (b'\x00\x00\x00\x01%\xb8 \x03\xbf\xff\xfe\x1e\x12('
               b'\x00\x08\x08\xfb\xef\xbe\xfb\xef\xbe\xfb\xef\xbe\xfb\xef\xbe\xfb\xef\xbe\xfb\xef\xbe\xfb\xef\xbe\xfb'
               b'\xef\xbe\xfb\xef\xbe\xfb\xef\xbe\xfb\xef\xbe\xfa\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
               b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
               b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
               b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
               b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
               b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
               b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
               b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
               b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
               b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
               b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
               b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
               b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
               b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
               b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
               b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
               b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
               b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
               b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
               b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
               b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
               b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
               b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae'
               b'\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
               b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xad_}\xf7\xdf}\xf7\xdf'
               b'}\xf5\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xdf}\xf7\xdf}u\xd7]u\xd7]u'
               b'\xd7]u\xd7]u\xd7]u\xd7]u\xd7Z\xbe\xf9{'
               b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xbe\xfb\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
               b'\xae\xba\xeb\xae\xba\xeb.>\xba\xeb\xbe\xfb\xef\xae\xba\xeb\xae\xba\xeb\xae\xba\xebu\xd7Z\xbe\xf6'
               b'\x9ely\xb1\xe9\x13h\x9du\xd7]u\xd7]u\xd7]u\xd7]\xf7\xdf}\xf7\xdf['
               b'O\xbe^\xfb\xeb\xae\xb3c\xef\xbe\xf6d\xebW\xab\xd4%\x87\xca\xae\xff\xff{'
               b'UD\xa6\x96\xd6E\xb5\xb7\xbeN\xfb\xef\xbe\xfb\xef\xbe\xfa\xeb\xae\xba\xd5\xf7\xde\xaf\xae\xb8\xef\xff'
               b'\xfd\xb7\x87r\xcf\xff\xf7?\x90\x9d\xf7\xdf}\xf5\xdf]u\xc8\xea\xbaz\xebu\xcd\xfa\x96\x96\x96\x96\x96'
               b'\x96\x96\x96\x96\x9e\xba\xeb\xae\xba\xeb\xad^L]u\xd7\x08\x7f\xa7\xff\xbca\xab\xe4\xc5k\xae\xba\xeb'
               b'\xae\xba\xeb\xbe\xb9\t\xb5\xbd\xd7]t\xf5\xd7]u\xd76\xadkkkKK]u\xd7/]u\xff\xff\xf0CU\xc7\xe5\xcf\xfe'
               b'\xc9\xdaw\nb[\xff4\xd9\xd9\x12\x95q\xc4\x98\xd8\xb3\xc2j\nxKe\xf5\xa9\x87\x0c\x1d\x8aH\xf5\xff\xe7'
               b']\x93\xf1\xea\xbd\xa1\xb4\xf7\xb2]\xe1\xe7Z\xe5-g\x1e\xa0&\xee\x80\xf57\xf4\xc62\x84\xcf\x98\xd7'
               b'\xa2iiiiiii\xeb\xae\xb99\x1e\xfa\xddu\xd7O]n\xba\xeb\xadS\x93\x1f{'
               b'\x06\xbb\xeb\xae\xba\xeb\xae\xba\xeb\x8f\xffO\xff&\xec\x97}\xad\xad\xf5\xd7]s~\xa5\xa5\xa5\x8eT\x7f'
               b'\xfd\x97\xa5\xb5\x93\xb5\xa5\xa5t\xb4\xb5\xd3\xd7]u\xdfkkkkkK]u\xd7]u\xd7]\xf4\xf5\xd7]-----=u\xd7}u'
               b'\xdf]u\xd7]t\xf7\xdf}\xf7\xdf}u\xd7]u\xd7]\xf5\xd7]u\xd3\xd7]u\xd7]u\xd3\xd7]u\xd7]\x13}\xf5\xd7]t'
               b'\xb4\xb4\xb4\xb4\xb4\xb4\xb4\xb6\xb5\xd3\xd7]u\xd7]u\xd7]t\xf5\xd7]u\xd7]t\xf5\xd7]u\xd7]u\xd7]u\xd7'
               b']u\xd7]u\xd7]=u\xd7]u\xd7]u\xd7O]u\xd7]u\xd7D\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]t\xf5\xd7]u\xd7]u'
               b'\xd7]=u\xd7]u\xd7]=u\xd7]u\xd2\xd14\xf5\xd7]u\xd7]u\xd7]u\xd7O]u\xd7]rm\xae\xba\xeb\xa7\xae\xba\xeb'
               b'\xae\xba\xeb\xa5\xae\x9e\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba&\xba\xeb'
               b'\xae\xba\xeb\xae\xba\xeb\xa7\xae\xba\xeb\xae\xba\xeb\xae\xbaZZZZz\xeb\xae\xba\xeb\xae\xba\xeb\xae'
               b'\xba\xeb\xae\xba\xe9\xeb\xae\xba\xeb\xae\xfa\xeb\xae\xbaz\xeb\xae\xba\xeb\xae\xba\xeb\xff\x9f\xa1'
               b'\xf0\xa7\x1a\xa2\xec\xf9\xc7f\xa7\xf4M\xd3\xc9\xbe?1\x1dK\xf6\x93\xff\x1f\xf3c\xe8\x7f\xf1\xeb\xd5'
               b'\x17e\xff\xfcC\xfd\x07\xbc\x989I\x98\xc2Lv\xff\xf8\xff\x7fM?\xf8\xac\xbf\xfeE\xd7]u\xd7]u\xd7]u\xd3'
               b'\xd7]u\xd7]u\xd7]t\xf5\xd7]u\xd7]u\xd7}u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]t\xf5\xd7]u\xd7]u\xd7]=u\xd7]u'
               b'\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]=u\xd7]u\xd7]u\xd7O]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u'
               b'\xd7]u\xd7O]u\xd7]u\xc9\xb6\xba\xeb\xa7\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb'
               b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xa7\xae\xba\xeb\xae\xba\xeb\xae\xba\xe9\xeb\xae\xb5}\xf7\xdf'
               b'}\xf7\xdf}u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]=u\xd7]u\xd7]u\xd7O]j\xba\xeb\xae\xba\xeb\xae\xba\xef\xbe'
               b'\xfb\xef\xbe\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xe9\xeb\xae\xba\xeb\xae\xbb\xeb\xae\xbaz\xd5u'
               b'\xd7]u\xd7]u\xd7]u\xd7]w\xd7]u\xd7]u\xd7]u\xd7O['
               b'\xae\xba\xeb\xae\xba\xeb\xae\xbau]u\xd7]u\xd7]u\xd7]u\xd7]u\xdf]u\xd7]u\xd7]u\xd7O]u\xd7]j\xfa\xeb'
               b'\xae\xb5O]u\xd7]u\xd7]u\xd7]d\xc7\x90\x92\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xe9\xeb'
               b'\xae\xba\xebU\xd7]m\xbe\xbaz\xeb\xae\xb4\x9e\x81\xbe\xfb\xefw\xdf/}\xf7\xdf}\xf7\xde\xef\xbe\xfb\xe5'
               b'\xef\xbd\xa7\xdf}\xf5\xbbz\xebW\xdf]u\xba\xef\xbe\xfb[[[[[[[[ZZZZZZZZZZZ[[[[[[['
               b'ZZZZZZZZZ\xdd\xf7\xdf}u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7'
               b']u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7\xf2\xff\xf8{'
               b'\x04Mb\xc1\xe5\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]w\xd7]u\xd7]u\xd7]u'
               b'\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7'
               b']u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u'
               b'\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7'
               b']u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u'
               b'\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7'
               b']u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u'
               b'\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7'
               b']u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]q\xdf\xfe\x9f\xeb\xae\xba\xeb\xae\xba\xe3\xbf\xff'
               b'\xef]u\xc7\x7f\xff\xee?\xff\xed\xb7\xb6o\xff\xfepC\x9b\xe3\xb2\x91\xffm\xbd\xbe\xbek\xcf?\x8c\xd5'
               b'\xfd\xa4\x97\x7f\x7f\xdb\xf8{\xdaO\xc4\x05mW\xfe\x08\xadV\xf1\xcf\xa7\xff\xffW\x0f\xff\x0fE\xfa\xeb'
               b'\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xff\xff\x8c;\xcd\x9cO+\xfd'
               b'?\xff\x1f\x82\x0fO\xff\xf1T\x82Y\xb3\xbf\xff['
               b'\xfc\x10V\x93\x84\x1f\xf5\xff\xfc}Wo\rq<\xe3\xdb\xdf\xfbq\xcea\x8e\x99+\x7f\xfe\xa2\xab\x12\xff\xc3'
               b'\x15\xdd\xfat\x10\xe9\xff\xff\xa9\xc6_\xfc\x15S\xafo\xa7\xae\xbb['
               b'Z\xe9k\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xbf\xff\xfe\x08z\xd7]u\xff\x88\x9e2\xeb'
               b'\xaa\xea\x9dt\xbb\xd1?1\xf1\xfd\x05\xb0\xbf\xd7y\xee\x9dF_\xff\x87\xa9\xf8\xf4\xab\xff\xc1U~\xdf('
               b'\xff\xfd\x87\xb7\xda\xda\xd7k}\xf7\xdf]u\xd7Y\x98]u\xd7]u\xd7]u\xd7Xw,'
               b'\xba\xeb\xae\x12\xc2m\x87\xfa\x7f\xde\xc9\x8fP\x8fZ\x8e\x9f\xff\xa7\xbe\xba\xeb\xae\x96\x96\x96\xbaZ'
               b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xef\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xbe\xba\xeb\xae\xd6\xd6'
               b'\x96\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae;\xff\xf6\xfdq\xdf\xff\xdf\xae;\xff\x7f\xf5\xd7\x1d\xdf\xff'
               b'\xfa\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xb8'
               b'\xef\xff\xf5\xd7\\wn\xcb\xff\xeb\xe7\x87\xff\x87\xb6\xf5\xd7]u\xd7]u\xd7]\x7f\xf3\xff\x87\xf5\xe7'
               b'\xfc\xcez\x8c\x12\xf6\xaf\x1f\x98\x97\xff\xe9\x93\xff\xfe\xb5@\x86\xdf:\x94\x8aT9\xff\xcb\xff\xd7]u'
               b'\xd7]u\xd7]u\xd7\\w\xfd\x7f\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\x8e\xff\xfd\xbf]u'
               b'\xd7]u\xfe\xab\xff\xc9\x1f/\xfd\x02\xab\x9fo\xad\xda\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xc7'
               b'\x7f\xff^\xb8\xef\xfd\xff\xd7_J\x87\xff\x91u\xd7]u\xd7kkK]u\xd7]u\xd7]u\xd7\\w\xfe\xbe\xf7\xae\xba'
               b'\xeb\xae\xba\xeb\xae\xb8\xec=\xd2\xf3\xd6O\xff]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]\xf1'
               b'\xdf\xaf\xff\xaf\xff\xff\x87\xf1\xeb\x1dz\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\x8e'
               b'\xff\xff\xbdu\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7_\xff\xff\x04>l]u\xd7]u\xdf]u\xd7]u'
               b'\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7\x1d\xff\xffn\xba\xeb\xae\xba\xeb\xbe\xba\xeb\xae\xba\xeb\xae\xba'
               b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\x8e\xff\xfa\xfd\x7f\xff\xf1\x87\xfc'
               b']u\xfe\x9f\xfe\x1f\xf7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xdf]u\xd7}u\xd7]u\xd7'
               b']u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u'
               b'\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7'
               b']u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7]u\xd7\\\xd91'
               b'\xe9\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba\xeb\xae\xba'
               b'\xeb\xae\xba\xeb\xae\xba\xeb\xae\xbaZ\xeb\xae\xba\xf0')

sps = b"\'B\x00\x1f\xab@Z\x05\x0c\x80"
pps = b'(\xce<\x80'


def test():
    payload = byte_string
    if byte_string.startswith(b'\x00\x00\x00\x01'):
        payload = byte_string[4:]

    unit_type = payload[0] & 0x1F
    nalu_length = len(payload)
    # Convert the length to a 4-byte big-endian format
    length_data = struct.pack('>I', nalu_length)
    frame_bytes = length_data + payload

    # Helper function to add NAL start codes
    def add_nal_start_code(data):
        return b'\x00\x00\x00\x01' + data

    # Constructing the H.264 byte stream
    h264_stream = add_nal_start_code(sps) + add_nal_start_code(pps) + byte_string
    print(h264_stream)
    print("\n====\n")
    print(other)

    # Write the H.264 stream to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".h264") as tmpfile:
        tmpfile.write(add_nal_start_code(sps) + add_nal_start_code(pps) + other)
        h264_filename = tmpfile.name

    # Now use cv2.VideoCapture to read frames from the temporary file
    cap = cv2.VideoCapture(h264_filename)

    # Reading frames from the H.264 stream
    if cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("boo")
            return

        print(frame)

        # Process the frame (for example, show it)
        cv2.imwrite("frame.png", frame)
        #
        # if cv2.waitKey(100) & 0xFF == ord('q'):
        #     break
    else:
        print("closed")

    # Cleanup
    # cap.release()
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    test()

