init python:
    import chess
    class ChessManager:
        def __init__(self, fen=None, moves_limit=10):
            self.board = chess.Board(fen) if fen else chess.Board()
            
            self.selected_square = None
            self.legal_targets = []
            
            self.moves_limit = moves_limit
            self.moves_made = 0

        @property
        def is_white_turn(self):
            return self.board.turn == chess.WHITE

        @property
        def is_success(self):
            return self.board.is_checkmate() and self.board.turn == chess.BLACK

        @property
        def is_failure(self):
            if self.moves_made >= self.moves_limit and not self.is_success:
                return True
            return self.board.is_game_over() and not self.is_success

        def get_piece_at(self, x, y):
            """Возвращает имя файла фигуры для клетки (x, y)"""
            square = chess.square(x, y)
            piece = self.board.piece_at(square)
            if not piece:
                return None
            
            color_prefix = "w" if piece.color == chess.WHITE else "b"
            piece_names = {
                'p': 'pawn', 'n': 'knight', 'b': 'bishop',
                'r': 'rook', 'q': 'queen', 'k': 'king'
            }
            return f"{color_prefix}_{piece_names[piece.symbol().lower()]}"

        def select_square(self, x, y):
            """Логика клика по клетке"""
            square = chess.square(x, y)
            
            if square in self.legal_targets:
                self.make_move(self.selected_square, square)
                return

            piece = self.board.piece_at(square)
            if piece and piece.color == self.board.turn:
                self.selected_square = square
                self.legal_targets = [m.to_square for m in self.board.legal_moves if m.from_square == square]
            else:
                self.selected_square = None
                self.legal_targets = []
            
            renpy.restart_interaction()

        def make_move(self, from_sq, to_sq):
            move = chess.Move(from_sq, to_sq)
            
            piece = self.board.piece_at(from_sq)
            if piece and piece.piece_type == chess.PAWN:
                if chess.square_rank(to_sq) in [0, 7]:
                    move.promotion = chess.QUEEN

            if move in self.board.legal_moves:
                self.board.push(move)
                self.moves_made += 1
                self.selected_square = None
                self.legal_targets = []
                renpy.restart_interaction()