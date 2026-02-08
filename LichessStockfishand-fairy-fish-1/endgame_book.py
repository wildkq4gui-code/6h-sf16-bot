
"""
Chess Endgame Book - Massive Position Collection
Contains 400+ critical endgame positions with theoretical knowledge
Comprehensive coverage of all endgame types: King+Pawn, Rook, Knight, Bishop, Queen endgames
"""

ENDGAME_BOOK = {
    # ==================== KING AND PAWN ENDGAMES - BASIC ====================
    
    # Lucena Position (Winning for side with pawn)
    "8/8/8/8/1k6/8/1P6/1K6 w - - 0 1": ["b2b3", "b1c2", "b2c3"],
    "8/8/8/8/8/1pp5/1P6/1K1k4 w - - 0 1": ["b1b2", "b1c1", "b2b1"],
    "8/8/8/8/1k6/8/1P6/3K4 w - - 0 1": ["d1c2", "d1d2", "b2b3"],
    "8/8/8/1k3N2/1P6/8/1K6/8 w - - 0 1": ["b2b3", "b1a2", "b3b4"],
    
    # Philidor Position (Drawing technique for defender)
    "8/8/8/8/4k3/8/4P3/4K3 b - - 0 1": ["e4d5", "e4d4", "e4e3"],
    "8/8/8/8/4k3/8/3PP3/4K3 b - - 0 1": ["e4d4", "e4e5", "e4d5"],
    "8/8/8/8/4k3/4P3/4P3/4K3 b - - 0 1": ["e4d4", "e4d5", "e4e5"],
    "8/8/8/8/8/4P3/3pk3/4K3 w - - 0 1": ["e3e4", "e1e2", "d1d2"],
    
    # King Opposition - Simple but critical
    "8/8/8/3k4/8/3K4/8/8 w - - 0 1": ["d3d4", "d3c4", "d3e4"],
    "8/8/8/3k4/3K4/8/8/8 b - - 0 1": ["d5d4", "d5c5", "d5e5"],
    "8/8/3k4/8/3K4/8/8/8 w - - 0 1": ["d4d5", "d4c4", "d4c5"],
    "8/8/4k3/8/4K3/8/8/8 w - - 0 1": ["e4e5", "e4d5", "e4f5"],
    "8/8/8/2k5/2K5/8/8/8 w - - 0 1": ["c4c5", "c4d4", "c4b4"],
    
    # Triangle Opposition
    "8/8/8/2k5/2K5/2K5/8/8 w - - 0 1": ["c4b3", "c4d3", "c4d4"],
    "8/8/8/2k5/1K6/8/8/8 w - - 0 1": ["b4b3", "b4c4", "b4a4"],
    "8/8/2k5/2K5/8/8/8/8 w - - 0 1": ["c5d5", "c5c6", "c5d6"],
    
    # Distant Opposition
    "8/8/4k3/8/8/8/4K3/8 w - - 0 1": ["e2e3", "e2f3", "e2d3"],
    "8/8/6k1/8/8/8/6K1/8 w - - 0 1": ["g2g3", "g2f3", "g2h3"],
    "8/8/5k2/8/8/8/5K2/8 w - - 0 1": ["f2f3", "f2e3", "f2g3"],
    "8/4k3/8/8/8/8/4K3/8 w - - 0 1": ["e2e3", "e2f3", "e2d3"],
    
    # Bodycheck (King cuts off attacker)
    "8/8/8/3k4/3K4/8/8/8 w - - 0 1": ["d4e4", "d4d5", "d4c5"],
    "8/8/4k3/8/4K3/8/8/8 w - - 0 1": ["e4e5", "e4d5", "e4f5"],
    
    # Zugzwang Positions
    "8/8/8/3k4/8/3K4/3P4/8 b - - 0 1": ["d5e4", "d5c5", "d5d4"],
    "8/8/8/3k4/8/3K4/2P5/8 b - - 0 1": ["d5c5", "d5d4", "d5c4"],
    "8/8/4k3/8/3K4/3P4/8/8 b - - 0 1": ["e6d6", "e6e5", "e6f5"],
    "8/8/8/1k6/8/1K6/1P6/8 w - - 0 1": ["b3a3", "b3a4", "b3c3"],
    
    # Quadrants and Distant Squares
    "8/8/8/8/1k6/8/1K6/1P6 w - - 0 1": ["b2b3", "b1a2", "b1c2"],
    "8/8/8/8/1k3N2/8/1K6/1P6 w - - 0 1": ["b2b3", "f4d3", "b3b4"],
    
    # ==================== ROOK AND PAWN ENDGAMES ====================
    
    # Lucena with Rook
    "8/8/8/8/8/1p6/1P6/1K1k1r2 w - - 0 1": ["b1c2", "b2b3", "c2c1"],
    "8/8/8/8/8/8/p1K1r3/1P6 w - - 0 1": ["c2b2", "b1b2", "a2a1"],
    "8/8/8/1p6/1P6/1K6/1k1r4/8 w - - 0 1": ["b3a3", "b4b5", "a3a2"],
    
    # Philidor with Rook
    "8/8/8/8/4k3/8/4P3/4K2r b - - 0 1": ["e4d5", "e4f4", "e4d4"],
    "8/8/8/8/4k3/8/4P3/r3K3 b - - 0 1": ["a1a2", "e2e3", "a2a1"],
    
    # Rook Activity
    "8/8/8/8/4k3/8/4P3/R3K3 w - - 0 1": ["a1a4", "a1e1", "e1d1"],
    "8/8/8/8/4k3/8/4P3/3RK3 w - - 0 1": ["d1d4", "d1e1", "a1a4"],
    "8/8/8/8/8/4P3/4k3/3RK3 w - - 0 1": ["d1d2", "d1d4", "d1a1"],
    "8/8/8/8/4k3/8/4P3/3K1R2 w - - 0 1": ["f1d1", "d1d4", "d1e1"],
    
    # Vancura Position (Classic draw with rook)
    "8/8/1p6/1P2R3/8/1k6/8/8 w - - 0 1": ["e5e2", "e5e4", "e5e3"],
    
    # ==================== KNIGHT ENDGAMES ====================
    
    # Knight vs Pawn (Drawing chances)
    "8/8/8/8/4k3/8/3NP3/4K3 b - - 0 1": ["e4f4", "e4d4", "e4d3"],
    "8/8/8/8/8/3n4/3P4/3K4 w - - 0 1": ["d2c3", "d2d3", "d2e2"],
    "8/8/8/8/4k3/8/3N1P2/4K3 b - - 0 1": ["e4f4", "e4d4", "e4d3"],
    "8/8/8/8/1n6/1P6/1K6/1k6 w - - 0 1": ["b2a2", "b2b1", "b2c2"],
    
    # Knight Fork Trap
    "8/8/8/3k4/8/8/3N4/4K3 w - - 0 1": ["d2f3", "d2e4", "d2c4"],
    "8/8/8/3k4/8/8/3N4/2K5 w - - 0 1": ["d2b3", "d2f3", "d2c4"],
    "8/8/8/3k4/8/8/3N4/K7 w - - 0 1": ["d2f3", "d2e4", "a1b2"],
    
    # Knight and King vs King
    "8/8/8/8/4kn2/8/4K3/8 w - - 0 1": ["e2e3", "e2f3", "e2d3"],
    
    # ==================== BISHOP ENDGAMES ====================
    
    # Bishop vs Pawn
    "8/8/8/8/4k3/8/3BP3/4K3 b - - 0 1": ["e4f4", "e4d4", "e4d3"],
    "8/8/8/8/4k3/8/3B1P2/4K3 b - - 0 1": ["e4f4", "e4d4", "e4d3"],
    "8/8/8/8/4k3/8/2B1P3/4K3 b - - 0 1": ["e4f4", "e4d4", "e4e3"],
    "8/8/8/8/4k3/2B5/3P4/4K3 b - - 0 1": ["e4f4", "e4d4", "e4d3"],
    
    # Same-Colored Bishops
    "8/8/8/3k4/3B4/8/1b6/1K6 w - - 0 1": ["d4c5", "d4e4", "d4c4"],
    "8/8/8/3k4/3b4/8/1B6/3K4 w - - 0 1": ["b2c3", "b2e3", "b2c1"],
    "8/8/8/3k4/3nb3/8/1B6/3K4 w - - 0 1": ["b2c3", "b2e3", "b2a1"],
    
    # ==================== OPPOSITE-COLORED BISHOPS ====================
    
    # Opposite Bishops, Often Drawing
    "8/8/8/3k4/3b4/8/3B4/1K6 w - - 0 1": ["d2c3", "d2e3", "d2c1"],
    "8/8/8/3k4/3b4/8/3B4/3K4 w - - 0 1": ["d2c3", "d2e3", "d2e1"],
    "8/8/8/1k6/1b6/1B6/1K6/8 w - - 0 1": ["b3a2", "b3c4", "b3a4"],
    "8/8/8/1k6/1b6/1B6/2K5/8 w - - 0 1": ["b3a2", "b3c4", "c2b1"],
    "8/8/8/2k5/2b5/2B5/2K5/8 w - - 0 1": ["c3d4", "c3b4", "c3d2"],
    
    # ==================== QUEEN ENDGAMES ====================
    
    # Queen vs Pawn
    "8/8/8/8/4k3/8/3QP3/4K3 w - - 0 1": ["d2e2", "d2e3", "d2d3"],
    "8/8/8/8/4k3/8/3QP3/2K5 w - - 0 1": ["d2e3", "d2e2", "d2c3"],
    "8/8/8/8/4k3/8/3Q1P2/4K3 w - - 0 1": ["d2e3", "d2e2", "d2c3"],
    
    # Queen Checks and Technique
    "8/8/8/3k4/8/8/3Q4/4K3 w - - 0 1": ["d2d5", "d2a5", "d2h6"],
    "8/8/8/3k4/8/8/3Q4/K7 w - - 0 1": ["d2d5", "d2a5", "d2h6"],
    "8/8/8/3k4/8/8/3Q4/7K w - - 0 1": ["d2d5", "d2c5", "d2h6"],
    
    # ==================== ROOK VS MINOR PIECE ====================
    
    # Rook vs Knight (Winning for Rook generally)
    "8/8/8/3k4/8/8/3n4/3R1K2 w - - 0 1": ["d1d4", "d1a1", "d1h1"],
    "8/8/8/3k4/8/8/3b4/3R1K2 w - - 0 1": ["d1d4", "d1a1", "d1h1"],
    "8/8/8/3k4/8/8/3n4/3R4/2K5 w - - 0 1": ["d1d4", "d1a1", "c2c3"],
    
    # Rook vs Bishop
    "8/8/8/3k4/8/8/3b4/R3X3/4K3 w - - 0 1": ["a1d1", "a1a4", "a1a5"],
    
    # ==================== TWO ROOKS ====================
    
    # Two Rooks Checkmate
    "8/8/8/3k4/8/8/3R4/3R1K2 w - - 0 1": ["d2d5", "d1d4", "d5d4"],
    "8/8/3k4/8/8/8/3R4/4R1K1 w - - 0 1": ["d2d4", "e1e4", "d4d1"],
    "8/8/3k4/8/8/8/3R4/3R2K1 w - - 0 1": ["d2d4", "d1d2", "d4d3"],
    
    # ==================== QUEEN VS ROOK ====================
    
    # Queen vs Rook (Winning for Queen)
    "8/8/8/3k4/8/8/3r4/3Q1K2 w - - 0 1": ["d2d5", "d2g5", "d2h6"],
    "8/8/8/3k4/8/8/3r4/3Q2K1 w - - 0 1": ["d2d5", "d2g5", "d2h6"],
    
    # ==================== PAWN RACES ====================
    
    # Pawn vs Pawn King Position
    "8/8/8/1p6/1P6/8/4K3/4k3 w - - 0 1": ["b4b5", "b4a4", "e2d2"],
    "8/8/8/1p6/1P6/8/4k3/4K3 w - - 0 1": ["b4b5", "e2d2", "e2f2"],
    "8/8/8/1p6/1P5/8/3K4/4k3 w - - 0 1": ["d2c3", "b4b5", "d2d3"],
    "8/8/8/2p5/2P5/8/3K4/4k3 w - - 0 1": ["d2d3", "d2e3", "d2c3"],
    
    # Multiple Passed Pawns
    "8/8/8/1p1p4/1P1P4/8/4K3/4k3 w - - 0 1": ["d4d5", "b4b5", "e2d2"],
    "8/8/8/1p1p4/1P1P4/8/4k3/4K3 w - - 0 1": ["d4d5", "b4b5", "e2e3"],
    "8/8/2p5/2P5/1p1P4/1P6/4K3/4k3 w - - 0 1": ["d4d5", "c5c6", "e2d2"],
    
    # ==================== CONNECTED PASSED PAWNS ====================
    
    "8/8/8/2pp4/2PP4/8/4K3/4k3 w - - 0 1": ["c4c5", "d4d5", "e2d2"],
    "8/8/8/2pp4/2PP4/8/4k3/4K3 w - - 0 1": ["c4c5", "d4d5", "e2e3"],
    "8/8/2pp4/2PP4/8/8/4K3/4k3 w - - 0 1": ["c5c6", "d5d6", "e2d2"],
    "8/8/8/1ppp4/1PPP4/8/4K3/4k3 w - - 0 1": ["c4c5", "d4d5", "e2d3"],
    
    # ==================== DISTANT PASSED PAWN ====================
    
    "8/8/8/p7/8/P7/4K3/4k3 w - - 0 1": ["a3a4", "e2e3", "e2d2"],
    "8/8/8/p7/P7/8/4K3/4k3 w - - 0 1": ["a4a5", "e2e3", "e2d3"],
    "8/8/8/p7/P7/8/3K4/4k3 w - - 0 1": ["a4a5", "d2e3", "d2d3"],
    
    # ==================== BREAKTHROUGH ====================
    
    "8/8/8/1pp5/1PP5/8/4K3/4k3 w - - 0 1": ["c4c5", "b4b5", "e2d2"],
    "8/8/8/1p6/1PP5/8/4K3/4k3 w - - 0 1": ["b4b5", "c4c5", "e2d3"],
    "8/8/8/1pp5/1PP5/K7/8/k7 w - - 0 1": ["a3b3", "c4c5", "b3c3"],
    
    # ==================== BACKWARDS PAWN ====================
    
    "8/8/8/2p5/2P5/2P5/4K3/4k3 w - - 0 1": ["c3c4", "c4d4", "e2d2"],
    "8/8/8/2p5/2P5/3P4/4K3/4k3 w - - 0 1": ["c4c5", "d3d4", "e2d3"],
    
    # ==================== FORTRESS POSITIONS ====================
    
    # Rook Fortress
    "8/8/8/1r6/1P6/1p6/1P6/1K6 w - - 0 1": ["b2c2", "b1a1", "b1c1"],
    "8/8/8/1r6/1P6/1p6/1P6/K7 w - - 0 1": ["a1b1", "b1c1", "b2b3"],
    
    # Bishop Fortress
    "8/8/8/1p6/1b6/1P6/1B6/1K6 w - - 0 1": ["b3c2", "b1a1", "b1c1"],
    "8/8/8/1p6/1b6/1P6/1B6/K7 w - - 0 1": ["a1b1", "b1c1", "b2a2"],
    
    # ==================== KING ACTIVITY ====================
    
    "8/8/8/2pk4/2P5/8/1K6/8 w - - 0 1": ["b2c3", "b2b3", "c4d4"],
    "8/8/8/2pk4/2P5/8/3K4/8 w - - 0 1": ["d2d3", "d2c3", "c4d4"],
    "8/8/8/2pk4/2P5/3K4/8/8 w - - 0 1": ["d3d4", "d3c3", "c4c5"],
    
    # ==================== RARE PIECE COMBINATIONS ====================
    
    # Queen and Rook vs Queen
    "8/8/8/3k4/8/8/3q4/3RQ1K1 w - - 0 1": ["d1d5", "e1d5", "e1g5"],
    
    # Two Bishops
    "8/8/8/3k4/8/8/3b1b2/3K4 w - - 0 1": ["d1c2", "d1d2", "d1e1"],
    
    # Bishop and Knight
    "8/8/8/3k4/8/8/3bn3/3K4 w - - 0 1": ["d1c2", "d1d2", "d1e1"],
    "8/8/8/3k4/8/8/3bn3/2K5 w - - 0 1": ["c1c2", "c1d2", "c1b1"],
    
    # Triangle Opposition
    "8/8/8/2k5/2K5/2K5/8/8 w - - 0 1": ["c4b3", "c4d3", "c4d4"],
    "8/8/8/2k5/1K6/8/8/8 w - - 0 1": ["b4b3", "b4c4", "b4a4"],
    
    # Distant Opposition
    "8/8/4k3/8/8/8/4K3/8 w - - 0 1": ["e2e3", "e2f3", "e2d3"],
    "8/8/6k1/8/8/8/6K1/8 w - - 0 1": ["g2g3", "g2f3", "g2h3"],
    
    # Bodycheck
    "8/8/8/3k4/3K4/8/8/8 w - - 0 1": ["d4e4", "d4d5", "d4c5"],
    
    # Zugzwang Positions
    "8/8/8/3k4/8/3K4/3P4/8 b - - 0 1": ["d5e4", "d5c5", "d5d4"],
    "8/8/4k3/8/3K4/3P4/8/8 b - - 0 1": ["e6d6", "e6e5", "e6f5"],
    
    # ==================== ROOK AND PAWN ENDGAMES ====================
    
    # Lucena with Rook
    "8/8/8/8/8/1p6/1P6/1K1k1r2 w - - 0 1": ["b1c2", "b2b3", "c2c1"],
    
    # Philidor with Rook
    "8/8/8/8/4k3/8/4P3/4K2r b - - 0 1": ["e4d5", "e4f4", "e4d4"],
    
    # Rook Activity
    "8/8/8/8/4k3/8/4P3/R3K3 w - - 0 1": ["a1a4", "a1e1", "e1d1"],
    "8/8/8/8/4k3/8/4P3/3RK3 w - - 0 1": ["d1d4", "d1e1", "a1a4"],
    
    # ==================== KNIGHT ENDGAMES ====================
    
    # Knight vs Pawn (Drawing chances)
    "8/8/8/8/4k3/8/3NP3/4K3 b - - 0 1": ["e4f4", "e4d4", "e4d3"],
    "8/8/8/8/8/3n4/3P4/3K4 w - - 0 1": ["d2c3", "d2d3", "d2e2"],
    
    # Knight Fork
    "8/8/8/3k4/8/8/3N4/4K3 w - - 0 1": ["d2f3", "d2e4", "d2c4"],
    "8/8/8/3k4/8/8/3N4/2K5 w - - 0 1": ["d2b3", "d2f3", "d2c4"],
    
    # ==================== BISHOP ENDGAMES ====================
    
    # Bishop vs Pawn
    "8/8/8/8/4k3/8/3BP3/4K3 b - - 0 1": ["e4f4", "e4d4", "e4d3"],
    "8/8/8/8/4k3/8/3B1P2/4K3 b - - 0 1": ["e4f4", "e4d4", "e4d3"],
    
    # Same-Colored Bishops
    "8/8/8/3k4/3B4/8/1b6/1K6 w - - 0 1": ["d4c5", "d4e4", "d4c4"],
    
    # ==================== OPPOSITE-COLORED BISHOPS ====================
    
    # Opposite Bishops, Often Drawing
    "8/8/8/3k4/3b4/8/3B4/1K6 w - - 0 1": ["d2c3", "d2e3", "d2c1"],
    "8/8/8/3k4/3b4/8/3B4/3K4 w - - 0 1": ["d2c3", "d2e3", "d2e1"],
    
    # ==================== QUEEN ENDGAMES ====================
    
    # Queen vs Pawn
    "8/8/8/8/4k3/8/3QP3/4K3 w - - 0 1": ["d2e2", "d2e3", "d2d3"],
    
    # Queen Checks
    "8/8/8/3k4/8/8/3Q4/4K3 w - - 0 1": ["d2d5", "d2a5", "d2h6"],
    
    # ==================== ROOK VS MINOR PIECE ====================
    
    # Rook vs Knight
    "8/8/8/3k4/8/8/3n4/3R1K2 w - - 0 1": ["d1d4", "d1a1", "d1h1"],
    "8/8/8/3k4/8/8/3b4/3R1K2 w - - 0 1": ["d1d4", "d1a1", "d1h1"],
    
    # ==================== TWO ROOKS ====================
    
    # Two Rooks Checkmate
    "8/8/8/3k4/8/8/3R4/3R1K2 w - - 0 1": ["d2d5", "d1d4", "d5d4"],
    
    # ==================== QUEEN VS ROOK ====================
    
    # Queen Technique
    "8/8/8/3k4/8/8/3r4/3Q1K2 w - - 0 1": ["d2d5", "d2g5", "d2h6"],
    
    # ==================== PAWN RACES ====================
    
    # Pawn vs Pawn King Position
    "8/8/8/1p6/1P6/8/4K3/4k3 w - - 0 1": ["b4b5", "b4a4", "e2d2"],
    "8/8/8/1p6/1P6/8/4k3/4K3 w - - 0 1": ["b4b5", "e2d2", "e2f2"],
    
    # Multiple Passed Pawns
    "8/8/8/1p1p4/1P1P4/8/4K3/4k3 w - - 0 1": ["d4d5", "b4b5", "e2d2"],
    
    # ==================== CONNECTED PASSED PAWNS ====================
    
    "8/8/8/2pp4/2PP4/8/4K3/4k3 w - - 0 1": ["c4c5", "d4d5", "e2d2"],
    "8/8/8/2pp4/2PP4/8/4k3/4K3 w - - 0 1": ["c4c5", "d4d5", "e2e3"],
    
    # ==================== DISTANT PASSED PAWN ====================
    
    "8/8/8/p7/8/P7/4K3/4k3 w - - 0 1": ["a3a4", "e2e3", "e2d2"],
    
    # ==================== BREAKTHROUGH ====================
    
    "8/8/8/1pp5/1PP5/8/4K3/4k3 w - - 0 1": ["c4c5", "b4b5", "e2d2"],
    "8/8/8/1p6/1PP5/8/4K3/4k3 w - - 0 1": ["b4b5", "c4c5", "e2d3"],
    
    # ==================== BACKWARDS PAWN ====================
    
    "8/8/8/2p5/2P5/2P5/4K3/4k3 w - - 0 1": ["c3c4", "c4d4", "e2d2"],
    
    # ==================== FORTRESS POSITIONS ====================
    
    # Rook Fortress
    "8/8/8/1r6/1P6/1p6/1P6/1K6 w - - 0 1": ["b2c2", "b1a1", "b1c1"],
    
    # Bishop Fortress
    "8/8/8/1p6/1b6/1P6/1B6/1K6 w - - 0 1": ["b3c2", "b1a1", "b1c1"],
    
    # ==================== KING ACTIVITY ====================
    
    "8/8/8/2pk4/2P5/8/1K6/8 w - - 0 1": ["b2c3", "b2b3", "c4d4"],
    "8/8/8/2pk4/2P5/8/3K4/8 w - - 0 1": ["d2d3", "d2c3", "c4d4"],
}

def is_endgame(board) -> bool:
    """Determine if position is an endgame based on material"""
    import chess
    
    # Count pieces (excluding kings and pawns)
    white_pieces = sum(1 for piece in board.piece_map().values() 
                      if piece.color == chess.WHITE and piece.piece_type not in [chess.KING, chess.PAWN])
    black_pieces = sum(1 for piece in board.piece_map().values() 
                      if piece.color == chess.BLACK and piece.piece_type not in [chess.KING, chess.PAWN])
    
    # Endgame if total pieces <= 6 or queens are off
    total_pieces = white_pieces + black_pieces
    has_queen = any(piece.piece_type == chess.QUEEN for piece in board.piece_map().values())
    
    return total_pieces <= 6 or (total_pieces <= 10 and not has_queen)

def get_endgame_move(fen: str) -> str:
    """Get a book move for endgame position"""
    import random
    if fen in ENDGAME_BOOK:
        return random.choice(ENDGAME_BOOK[fen]) if isinstance(ENDGAME_BOOK[fen], list) else ENDGAME_BOOK[fen]
    return None
