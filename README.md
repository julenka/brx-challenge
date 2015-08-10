This is a practical crypto reverse engineering challenge to try.

I recently discovered the Bluno Nano microcontroller, which has a built-in Bluetooth antenna. I was curious how this worked so I looked at the firmware file. But, the firmware is encrypted somehow. In order to start analyzing the file I had to decrypt it first.

Your challenge, should you accept it, is to decrypt this firmware. I've attached the firmware file. 

The four files inside the rar are firmware files and all are encrypted the same way.

Once you decrypt it, tell me which pin switch02 is connected to.

#### Observations
* The sequence b7 ff aa b6 be a8 b1 b8 repeats itself a lot at the end of the file. 
	* It's padded in some weird way.
	* 8 bytes
	* most likely padded with zeros, and then xor'd with an 8 byte key?

* `hexdump -c | less` gives the below output, and it turns out you can buy a bluno nano device from DFRobot!

```
0000000   D   F   R   o   b   o   t  \0  \0   <B8> 003  \0  \0  \0  \0  \0
0000010  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0
*
0000040
```

* Could be that data doesn't start until offset 000040
* length of each file in bytes:
	for f in *; do du -h $f; done
	240K	SBL_BlEMEGA2560V1.94.bin
	240K	SBL_BleMEGA1280V1.94.bin
	240K	SBL_BlelinkV1.94.bin
	240K	SBL_BlunoV1.94.bin

#### [DONE] Step 0: Convert .bin to .rar
* [forensicswiki](http://forensicswiki.org/wiki/RAR) says rar file has magic number of `0x 52 61 72 21 1A 07 00`, but this is not found in the file.
* probably need to figure out how to convert the file (minus padding) so that the code at offset 0000040 starts with the .rar magic number. Have no idea how to go about doing this.
* Turns out robert gave me the wrong file.

#### [DONE] Step 1: trim the first 64 bytes
* Also tried trimming first 208 bytes since data actually repeated until then

#### [DONE] Step 2: XOR with b7 ff aa b6 be a8 b1 b8

0 xor 0 = 0
0 xor 1 = 1

#### [DONE] Step 3: XOR with ~ (b7 ff aa b6 be a8 b1 b8) to get padding to be ones

#### Step 4: Get ASCII

`for f in decrypted/*; do strings $f; done`

Then find the stuff that looks like "switch 2" and copy only those lines

#### Step 5: Unscramble resulting ASCII

`unscramble.py strings_scrambled.txt`

#### Reading bytes in python
```
result = array.array('l')
while True:
	try:
		result.fromfile(f, 1000)
	except EOFError:
		break
```

* 'l' typecode is 8 bytes long, use 'c' typecode instead