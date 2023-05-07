import json
def save_play(self):
        # 실행중이던 세팅 설정을 딕셔너리 형태로 저장
        with open('game_data','w') as game_data_file: 
            json.dump(self.data, game_data_file)   


            