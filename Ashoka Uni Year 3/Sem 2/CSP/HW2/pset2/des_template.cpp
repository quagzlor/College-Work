#include<bits/stdc++.h>
using namespace std;
void print_byte(char byte) // Debugging purposes.
{
	for(int i=7;i>=0;i--)
	{
		if(byte&(1<<i))
		{
			cout<<"1";
		}
		else
		{
			cout<<"0";
		}
	}
	cout<<" ";
}
void print_byte_sequence(string s)
{
	for(int i=0;i<s.length();i++)
	{
		print_byte(s[i]);
	}
	cout<<'\n';
}
vector<vector<vector<int> >> sboxes; // First dimension is which sbox, second dimension is row, third dimension is column
void populate_sboxes()
{
	sboxes.resize(8);
	for(int i=0;i<sboxes.size();i++)
	{
		sboxes[i].resize(4);
		for(int j=0;j<sboxes[i].size();j++)
		{
			sboxes[i][j].resize(15);
		}
	}
	sboxes[0][0] = {14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7};
	sboxes[0][1] = {0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8};
	sboxes[0][2] = {4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0};
	sboxes[0][3] = {15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13};

	sboxes[1][0] = {15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10};
	sboxes[1][1] = {3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5};
	sboxes[1][2] = {0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15};
	sboxes[1][3] = {13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9};

	sboxes[2][0] = {10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8};
	sboxes[2][1] = {13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1};
	sboxes[2][2] = {13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7};
	sboxes[2][3] = {1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12};

	sboxes[3][0] = {7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15};
	sboxes[3][1] = {13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9};
	sboxes[3][2] = {10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4};
	sboxes[3][3] = {3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14};

	sboxes[4][0] = {2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9};
	sboxes[4][1] = {14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6};
	sboxes[4][2] = {4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14};
	sboxes[4][3] = {11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3};
	
	sboxes[5][0] = {12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11};
    sboxes[5][1] = {10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8};
    sboxes[5][2] = {9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6};
    sboxes[5][3] = {4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13};

    sboxes[6][0] = {4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1};
    sboxes[6][1] = {13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6};
    sboxes[6][2] = {1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2};
    sboxes[6][3] = {6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12};

    sboxes[7][0] = {13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7};
    sboxes[7][1] = {1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2};
    sboxes[7][2] = {7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8};
    sboxes[7][3] = {2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11};
}
// Some useful functions. Read https://en.wikipedia.org/wiki/DES_supplementary_material

// =============End============== //

string expansion(string halfblock) // takes 4 byte string and returns 6 byte string. First byte has been done for you
{
	// Converts to 31 0 1 2 3 4 | 3 4 5 6 7 8 | 7 8 9 10 11 12 11 12 13 14 15 16 15 16 17 18 19 20 19 20 21 22 23 24 23 24 25 26 27 28 27 28 29 30 31 0
	string expanded_halfblock = "      ";
	expanded_halfblock[0] = ((halfblock[3]&1)<<7)|((0xf8&halfblock[0])>>1)|((0x18&halfblock[0])>>3); // 31 0 1 2 3 4 3 4
	return expanded_halfblock;
}

string substitute(string keymixed_halfblock) // keymixed_halfblock has 6 bytes. First two Sbox substitutions have been done for you.
{
	string substituted_halfblock = "    ";

	// First S-Box takes first 6 bits. First we extract the first and sixth bit to figure out which row, then the middle four bits column to 
	// find the replacement.

	int row_val = ( (0x80&keymixed_halfblock[0]) >> 6)|( (0x04&keymixed_halfblock[0]) >> 2);

	int column_val = ( (0x78&keymixed_halfblock[0]) >> 3);

	substituted_halfblock[0] = sboxes[0][row_val][column_val];

    // Second S-Box substitution. 

    row_val = ( (0x02)&keymixed_halfblock[0]) |( (0x10&keymixed_halfblock[1]) >> 4);

    column_val = ( (0x01&keymixed_halfblock[0]) <<3)|( (0xe0&keymixed_halfblock[1]) >> 5);

    substituted_halfblock[0] = (substituted_halfblock[0]<<4)|(sboxes[1][row_val][column_val]);

    return substituted_halfblock;
}

string key_mixing(string expanded_halfblock, string subkey)
{
	// Xor the expanded halfblock with the key here. 
}

string permute(string substituted_halfblock) // takes 4 bytes string returns 4 bytes string. The first byte has been done for you
{
	string permuted_halfblock = "    ";
	// 16 7 20 21 29 12 28 17
	permuted_halfblock[0] = ((substituted_halfblock[1]&0x01) << 7) | ( (substituted_halfblock[0]&0x02) << 5) | ( (substituted_halfblock[2]&0x18) << 1) | ( (substituted_halfblock[3]&0x08)) | ( (substituted_halfblock[1]&0x10) >> 2) | ( (substituted_halfblock[3]&0x10) >> 3) | ( (substituted_halfblock[2]&0x80) >> 7);
	return permuted_halfblock;
}

string feistel_function(string halfblock, string subkey) // Accepts half a block and outputs half a block
{
	//expand => key mix => substitute => permute
}

string get_text(string filename) // Returns the plaintext string in bits.
{
	ifstream infile;
	infile.open(filename, ios::in);
	string s;
	infile>>s;
	return s;
}

vector<string> derive_round_subkeys(string key, bool decryption=false) // run in decryption = true to get the reverse round keys
{
	vector<string> round_subkeys(16);
	// Do work here
	return round_subkeys;
}
void swap(string &a, string &b)
{
	string temp = a;
	a = b;
	b = temp;
}

void xor_string(string &a, string b)
{
	for(int i=0;i<a.length();i++)
	{
		a[i] ^= b[i];
	}
}

string feistel_network(string block, string key, bool decryption_flag=false) // Applies Feistel network on eight bytes block
{
	vector<string> subkeys = derive_round_subkeys(key, decryption_flag);
	string first_halfblock = block.substr(0,4);
	string second_halfblock = block.substr(4,4);
	// Run the Feistel network for 16 rounds over here.
	return (first_halfblock+second_halfblock);
}

string des_cbc_encrypt(string plaintext, string key ,string initial_vector="abcdefgh")
{
	string ciphertext = "";
	// Do work here
	return ciphertext;
}

string des_cbc_decrypt(string ciphertext, string key, string initial_vector="abcdefgh")
{
	string plaintext = "";
	// Do work here
	return plaintext;
}

bool is_valid_key(string key) // Only length check (64 bits) - for now we ignore parity check.
{
	if(key.length()!=8)
	{
		return false;
	}
}

void pad_plaintext(string &plaintext) // Modifies inplace. PKCS5 padding. (Note that this is a function that uses call by reference)
{	
	/*
	Examples of PKCS5 padding for block length B = 8:

	3 bytes: FDFDFD           --> FDFDFD0505050505
	7 bytes: FDFDFDFDFDFDFD   --> FDFDFDFDFDFDFD01
	8 bytes: FDFDFDFDFDFDFDFD --> FDFDFDFDFDFDFDFD0808080808080808
	*/

	// example used from the CryptoSysk PKI Pro Manual, https://cryptosys.net/pki/manpki/pki_paddingschemes.html
	int pad_value = (8 - plaintext.length()%8); // pad with pad_value, pad_value times. 
	char pad_value_character = char(pad_value);
	for(int i=0;i<pad_value;i++)
	{
		// What do we put here?
	}
}


int main()
{
	string plaintext = get_text("plaintext.txt");
	string key_string = get_text("key.txt");
	populate_sboxes();
	pad_plaintext(plaintext);
	string s = "romeoandjulietweregreatlovers";
	pad_plaintext(s);
	string l = "Z8tb;a=";
	string k = des_cbc_encrypt(s, l);
	print_byte_sequence(s);
	print_byte_sequence(k);
	print_byte_sequence(des_cbc_decrypt(k, l));
}
