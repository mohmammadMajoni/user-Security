class Security:
    
    def secure(self, info):
        all_info = info.split(" ")
        return_text = ''
        
        for index in range(len(all_info)) :
            edit = (self.is_social_account_info(all_info[index])) 
            if edit : 
                all_info[index] = f'{all_info[index][:all_info[index].find(":")]}:{all_info[index][all_info[index].find(":") + 1 : all_info[index].find("/")]}/{self.encrypt(all_info[index][(all_info[index].find("/") + 1) : len(all_info[index])])}'
            return_text += f'{all_info[index]}'
            if index != (len(all_info) - 1) : return_text += ' '
            
        return return_text

    def is_social_account_info(self, param):
        try :
            if param.find(':') == -1 or param.find('/') == -1 : return False
            info = [param[:param.find(':')] , param[param.find(':') + 1 : param.find('/')] , param[(param.find('/') + 1) : len(param)]]
        except :
            return False
        if len(info[1]) == 0 or len(info[2]) == 0 or info[1][:3] != 'www' : return False
        if(65 <= ord(info[0][0]) <= 90) == False : 
            return False
        for letter in info[1] :
            letter = ord(letter)
            if(97 <= letter <= 122) or (48 <= letter <= 57) or letter == 46 :
                pass
            else : return False
        for letter in info[2] :
            letter = ord(letter)
            if(97 <= letter <= 122) or (48 <= letter <= 57) or letter == 95 or (65 <= letter <= 90) :
                pass
            else : return False
        return True
    
    def encrypt(self, s):
        if len(s) == 0 : return ''
        uniform = []
        let = s[0]
        startindex = 0
        for index in range(len(s)) :
            if s[index] != let :
                uniform.append(s[startindex:index])
                try :
                    startindex = index
                    let = s[index]
                except :
                    uniform.append(s[index])   
        try :
            if let != uniform[len(uniform) -1] : uniform.append(s[startindex:])
        except :
            uniform.append(s)  
             
        encrypted = ''
        sum = ''

        for uni in uniform :
            for index in range(len(uni)) :
                sum += str((ord(uni[index]) - 96) * (index + 1)) 
            encrypted += sum
            sum = ''
        return encrypted