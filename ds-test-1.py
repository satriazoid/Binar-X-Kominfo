def main(list_input):
    # Write your code here
    
    # urutkan datanya
    list_input_ = sorted(list_input, key=len) # len = menghitung panjang elemen
    
    # cari posisi/indeks median
    median = len(list_input_) // 2 # pembagi bilangan bulat
    string = list_input_[median]
    index = list_input.index(string) + 1
    return string, index
if __name__ == "__main__":
    list_of_strings = input().split(' ')
    # print(list_of_strings)
    string_out, index_out = main(list_of_strings)
    print(string_out)
    print(index_out)