# -*- coding: utf-8 -*-



from GomokuTrain import GomokuEnvironment, X, W1, b1, input_layer, W2, b2, hidden_layer, W3, b3, output_layer, Y, cost, optimizer
import tensorflow.compat.v1 as tf
import numpy as np
import random
import math
import os
import sys
import time

tf.disable_v2_behavior()

#------------------------------------------------------------
# 변수 설정
#------------------------------------------------------------
STONE_NONE = 0
STONE_PLAYER1 = 1
STONE_PLAYER2 = 2

gridSize = 10
#------------------------------------------------------------



#------------------------------------------------------------
# 화면 출력 함수
#------------------------------------------------------------
def showBoard(env):
	for y in range(gridSize):
		for x in range(gridSize):
			if( env.state[y * gridSize + x] == STONE_PLAYER1 ):
				sys.stdout.write('O')
			elif( env.state[y * gridSize + x] == STONE_PLAYER2 ):
				sys.stdout.write('X')
			else:
				sys.stdout.write('.')
		sys.stdout.write('\n')
	sys.stdout.write('\n')


#------------------------------------------------------------



#------------------------------------------------------------
# 게임 플레이 함수
#------------------------------------------------------------
def playGame(env, sess):

	env.reset()

	gameOver = False
	currentPlayer = STONE_PLAYER1
		
	while( gameOver != True ):
		action = - 9999
		
		if( currentPlayer == STONE_PLAYER1 ):
			currentState = env.getState()
		else:
			currentState = env.getStateInverse()

		action = env.getAction(sess, currentState)
		nextState, reward, gameOver = env.act(currentPlayer, action)
		
		showBoard(env)
		time.sleep(.5)
		
		if( currentPlayer == STONE_PLAYER1 ):
			currentPlayer = STONE_PLAYER2
		else:
			currentPlayer = STONE_PLAYER1
#------------------------------------------------------------



#------------------------------------------------------------
# 메인 함수
#------------------------------------------------------------
def main(_):

	# 환경 인스턴스 생성
	env = GomokuEnvironment(gridSize)

	# 텐서플로우 초기화
	sess = tf.Session()
	sess.run(tf.global_variables_initializer())

	# 세이브 설정
	saver = tf.train.Saver()

	# 모델 로드
	if( os.path.isfile(os.getcwd() + "/GomokuModel.ckpt.index") == True ):
		saver.restore(sess, os.getcwd() + "/GomokuModel.ckpt")
		print('Model loaded')
	
	# 게임 플레이
	playGame(env, sess)
	
	# 세션 종료
	sess.close()
#------------------------------------------------------------



#------------------------------------------------------------
# 메인 함수 실행
#------------------------------------------------------------
if __name__ == '__main__':
	tf.app.run()
#------------------------------------------------------------

