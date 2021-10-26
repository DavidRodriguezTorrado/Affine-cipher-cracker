# Developed by David Rodriguez

Text_to_decode = 'YDBCX UDBRN VBUIX KPNVU VKVIA TMDBW IVJXI TEXRX BXYXB RNMVI ' \
                 'VBLIV ONVIE XYXJX IIVIX CVYDB ADRQI VB '

def affine():
    print('Starting to decode...')

    text = Text_to_decode.replace(" ", "").lower()
    dictionary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Formula: X = inverse(a) (y-b) mod 26
    A = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    A_inv = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]

    string_result = ''
    for b in range(26):
        string_result = ''
        for a in A_inv:
            string_result = ''
            for i in range(len(text)):
                y = dictionary.index(text[i])
                next_letter = dictionary[(a *(y - b)) % 26]
                string_result = string_result + str(next_letter)
                A_original = A[A_inv.index(a)]
            print('Key a = {}; key b = {}; inv_a = {}; String_result: {}'.format(A_original, b, a, string_result))

if __name__ == '__main__':
    affine()

