import os

class SmartPhone():
    def __init__(self):

        self.__nameLst = []
        self.__numberLst = []
        self.__companyLst = []

        self.clearScreen()

        self.myPhone = input('먼저 사용자 이릅을 입력 해 주세요 > ')
        input(f'\n안녕하세요 {self.myPhone}님')

        self.clearScreen()

        while True:
            try:
                menu_number = int(input('번호를 눌러 메뉴를 선택해 주세요.\n\n'
                                        '1. 전화번호 저장\n'
                                        '2. 전화번호부 보기\n'
                                        '3. 전화번호 찾기\n'
                                        '4. 종료\n\n'))
            except Exception as e:
                self.clearScreen()

                menu_number = 0
            
            if menu_number == 1:
                self.clearScreen()

                try:
                    self.setData = input('저장 하려는 사용자의 정보를 입력 해 주세요.\n'
                                        '예) 홍길동,010-0000-0000,카카오 > ').strip().split(',')
                    if (len(self.setData) != 3):
                        self.clearScreen()

                        input('잘 못 입력하셨습니다.\n'
                              '예시와 같이 정확히 입력해 주세요.\n'
                              'Enter를 누르면 메인매뉴로 돌아갑니다.')
                        
                        self.clearScreen()
                        continue
                    
                    elif (self.setData[1].count('-') != 2):
                        self.clearScreen()

                        input('잘 못 입력하셨습니다.\n'
                              '예시와 같이 번호를 정확히 입력해 주세요.\n'
                              'Enter를 누르면 메인매뉴로 돌아갑니다.')
                        
                        self.clearScreen()
                        continue

                    self.inputData(self.setData)

                except Exception as e:
                    input('잘 못 입력하셨습니다.\n'
                          '예시와 같이 정확히 입력해 주세요.\n'
                          'Enter를 누르면 메인매뉴로 돌아갑니다.')

            elif menu_number == 2:
                self.clearScreen()

                for i, j, k in zip(self.__nameLst, self.__numberLst, self.__companyLst):
                    print(i, j, k)
                    print('----------')

                input('\nEnter를 눌러 이전화면으로 돌아가세요.')

            elif menu_number == 3:
                self.clearScreen()

                name = input('저장된 사용자 이름을 정확히 입력해 주세요. > ')
                print()

                if name in self.__nameLst:
                    index = self.__nameLst.index(name)
                    print(self.__nameLst[index], self.__numberLst[index], self.__companyLst[index])
                else:
                    print(f'{name}님은 저장되어있지 않습니다.')

                input('\nEnter를 눌러 이전화면으로 돌아가세요.')
                

            elif menu_number == 4:
                self.clearScreen()
                print('핸드폰을 종료합니다.')
                break

            else:
                self.clearScreen()

                input('숫자를 정확히 입력해 주세요!')
            
            self.clearScreen()

    def inputData(self, setData: list):
        self.clearScreen()

        self.phoneOwner(setData[0])
        self.phoneNumber(setData[1])
        self.company(setData[2])

        input('저장이 성공적으로 되었습니다.\n'
              '메뉴로 돌아가려면 Enter를 눌러주세요.')

    def phoneOwner(self, name):
        return self.__nameLst.append(name)

    def phoneNumber(self, num):
        return self.__numberLst.append(num)

    def company(self, C_name):
        return self.__companyLst.append(C_name)
    
    def clearScreen(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        
        os.system(command)

if __name__ == '__main__':
    myPhone = SmartPhone()
    
