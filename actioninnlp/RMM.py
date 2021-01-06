# 正向最大匹配
class RMM(object):
    def __init__(self, dic_path):
        self.dictionary = set()
        self.maximum = 0
        # 读取词典
        with open(dic_path, 'r', encoding='utf8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                if len(line) > self.maximum:
                    self.maximum = len(line)

    def cut(self, text):
        result = []
        index = 0
        while index < len(text):
            word = None
            for size in range(self.maximum, 0, -1):
                if index + size < 0:
                    continue
                piece = text[index:(index + size)]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index += size
                    break
            if word is None:
                index += 1
        return result[::-1]


def main():
    text = "南京市长江大桥"

    tokenizer = RMM('./data/imm_dic.utf8')
    print(tokenizer.cut(text))


main()
