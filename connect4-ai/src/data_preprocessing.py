# src/data_preprocessing.py

import numpy as np
from typing import List, Tuple
import pickle
import os
from game import Board

class MinimaxPlayer:
    def __init__(self, depth=8):
        self.depth = depth
    
    def minimax(self, board, depth, alpha, beta, maximizing):
        if depth == 0 or board.is_terminal():
            return self.evaluate(board), None
            
        if maximizing:
            max_eval = float('-inf')
            best_move = None
            for move in board.get_valid_moves():
                board_copy = board.copy()
                board_copy.make_move(move)
                eval, _ = self.minimax(board_copy, depth-1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf') 
            best_move = None
            for move in board.get_valid_moves():
                board_copy = board.copy()
                board_copy.make_move(move)
                eval, _ = self.minimax(board_copy, depth-1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

def generate_training_data(num_games: int = 1000) -> List[Tuple[np.ndarray, int]]:
    training_data = []
    minimax = MinimaxPlayer(depth=8)
    
    for game in range(num_games):
        board = Board()  # Your Connect4 board implementation
        while not board.is_terminal():
            state = board.get_state()
            _, move = minimax.minimax(board, 8, float('-inf'), float('inf'), True)
            training_data.append((state, move))
            board.make_move(move)
            
    return training_data

def save_training_data(data: List[Tuple[np.ndarray, int]], filename: str):
    os.makedirs('data/processed', exist_ok=True)
    with open(f'data/processed/{filename}', 'wb') as f:
        pickle.dump(data, f)

if __name__ == "__main__":
    # Generate 1000 games worth of training data
    training_data = generate_training_data(1000)
    save_training_data(training_data, 'minimax_training_data.pkl')