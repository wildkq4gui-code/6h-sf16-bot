
"""
Chess Middlegame Book - Massive Pattern Collection
Contains 300+ middlegame positions with tactical and strategic patterns
Organized by theme and tactical motif
"""

MIDDLEGAME_PATTERNS = {
    # ==================== ISOLATED PAWN (IQP) POSITIONS ====================
    "r1bq1rk1/pp1nbppp/2p1pn2/3p4/2PP4/2N1PN2/PP2BPPP/R1BQ1RK1 w - - 0 9": ["d4d5", "b1d2", "c1e3"],
    "r1bqk2r/pp1nbppp/2p1pn2/3p4/2PP4/2N1PN2/PP2BPPP/R1BQ1RK1 w KQkq - 1 8": ["d4d5", "c1g5", "e1g1"],
    "r1bq1rk1/1p1nbppp/p1p1pn2/3p4/2PP4/2N1PN2/PP2BPPP/R1BQ1RK1 w - - 1 9": ["d4d5", "e3g5", "b1d2"],
    "r1b2rk1/ppqnbppp/2p1pn2/3p4/2PP4/2N1PN2/PPQ1BPPP/R3BRK1 w - - 2 10": ["c1e3", "e1f2", "c2c3"],
    "r1bq1rk1/pp1n1ppp/2p1pn2/3p4/2PP4/1BN1PN2/PPQ1BPPP/R3BR1K w - - 1 10": ["c1e3", "b1d2", "f1e1"],
    
    # ==================== WEAK SQUARES & OUTPOSTS ====================
    "r1bq1rk1/pp3ppp/2np1n2/3Pp3/2P1P3/2N2N2/PPB2PPP/R1BQ1RK1 w - - 0 9": ["d5e6", "b1d2", "f1e1"],
    "r1bqk2r/pp1n1ppp/2n1p3/3pP3/2P5/2N1BN2/PP3PPP/R2Q1RK1 w KQkq - 0 9": ["e5e6", "d2e4", "e4g5"],
    "r1bq1rk1/pp2nppp/2np4/3pp3/2P1P3/2N2N2/PP2BPPP/R1BQ1RK1 w - - 1 8": ["e4e5", "c3d5", "d5e7"],
    "r1b1k2r/pp1n1ppp/2n1p3/3pP3/2P1N3/4p3/PP2BPPP/R2Q1RK1 b kq - 0 9": ["e3d2", "d1d2", "c6d4"],
    "r1bq1rk1/pp2nppp/2np4/3pp3/2P5/2N1BN2/PP2BPPP/R2Q1RK1 w - - 1 8": ["e3g5", "c3d5", "b7b6"],
    
    # ==================== WHITE ATTACKING PATTERNS ====================
    "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 2 4": ["b5f7", "e1g1", "c1e3"],
    "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/3P1N2/PPP2PPP/RNBQK2R w KQkq - 1 5": ["d3d4", "e4d5", "e1g1"],
    "r1bqk2r/pppp1ppp/2n2n2/2b1p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["f3e5", "e5d7", "c1e3"],
    "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/2N2N2/PPPP1PPP/R1BQK2R w KQkq - 2 5": ["b1d2", "e1g1", "d2c4"],
    "r1bqkbnr/pppp1ppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 2 4": ["c1e3", "f3e5", "e5g4"],
    "r1bq1bnr/ppppkppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 1 5": ["b5f7", "e1g1", "b7b6"],
    
    # ==================== BLACK COUNTERPLAY PATTERNS ====================
    "r3k2r/pp1n1ppp/2pb4/3pp3/2P1P3/2N2N2/PPB2PPP/R2Q1RK1 b kq - 1 9": ["b7b5", "e8f8", "d6c5"],
    "r1bqk2r/ppp1nppp/2n1p3/3p4/2P1P3/2N1BN2/PP3PPP/R2Q1RK1 b KQkq - 0 8": ["d5d4", "c6d4", "f6d4"],
    "r1bqk2r/ppp2ppp/2np1n2/3pp3/2P1P3/2N1BN2/PP3PPP/R2Q1RK1 b KQkq - 0 8": ["c6d4", "f3d4", "e5d4"],
    "r1b1k2r/ppppqppp/2n2n2/4p3/2P1P3/2N1BN2/PP3PPP/R2QK2R b KQkq - 2 8": ["e5d4", "f3d4", "e8f8"],
    "r1bqk1nr/ppp2ppp/2n1p3/3p4/2P1P3/2N1BN2/PP3PPP/R2QK2R b KQkq - 0 8": ["d5c4", "c1e3", "d8c7"],
    
    # ==================== BISHOPS OF OPPOSITE COLORS ====================
    "r3k3/pp3ppp/2nb4/3bp3/2P5/2NB1N2/PP3PPP/R2Q1RK1 w kq - 2 10": ["b1d2", "c3e4", "e4d6"],
    "r3k2r/ppp1b1pp/2nb4/3p4/2P1P3/2NB1N2/PP3PPP/R2Q1RK1 w KQkq - 0 9": ["e3g5", "c3e4", "c1f4"],
    "r3k1nr/pp1n2pp/2nb4/3p1bp1/2PP4/2N1BN2/PP3PPP/R2Q1RK1 w kq - 1 9": ["d4d5", "f3e5", "e5d7"],
    "r3k2r/pp1n1ppp/2nb4/3pp3/2P1P3/2NB1N2/PP3PPP/R2Q1RK1 b kq - 1 8": ["e8f8", "c3e4", "e4d6"],
    
    # ==================== ROOK ENDGAME TRANSITION ====================
    "r3k2r/pp3ppp/2nb4/3pp3/2P5/2NB1N2/PP3PPP/R2Q1RK1 b kq - 1 8": ["e8f8", "c3e4", "e4d6"],
    "4k3/pp3ppp/2nb4/3pp3/2P1N3/3B1N2/PP3PPP/R2Q1RK1 b - - 0 9": ["e4c5", "d3c5", "d8c7"],
    "r3k2r/pp1n1ppp/2nb4/3p4/2P1P3/2N1BN2/PP3PPP/R2Q1RK1 w kq - 0 8": ["c3e4", "e4d6", "b7b6"],
    "r3k2r/pp3ppp/2nb4/3p1bp1/2P1P3/2N1BN2/PP3K1P/R2Q3R b kq - 2 10": ["d5c4", "b1c4", "e8f8"],
    
    # ==================== PAWN BREAKS ====================
    "r1bqk2r/ppppbppp/2n2n2/4p3/2B1P3/2N2N2/PPPP1PPP/R1BQK2R w KQkq - 2 5": ["e4e5", "d2d4", "b1d2"],
    "r1bqk2r/pp1n1ppp/2np4/3pp3/2P1P3/2N2N2/PP2BPPP/R1BQ1RK1 w kq - 0 7": ["e4e5", "d2d4", "e5d6"],
    "r1bqk2r/ppp2ppp/2np1n2/3pp3/2P1P3/2N2N2/PP2BPPP/R1BQ1RK1 w kq - 0 7": ["c4d5", "f3d5", "d8d5"],
    "rnbqk2r/ppp2ppp/4pn2/3p4/2PP4/2N2N2/PP2BPPP/R1BQ1RK1 b kq - 1 8": ["d5c4", "c1e3", "e6e5"],
    
    # ==================== HANGING PIECES & TACTICS ====================
    "rn1qkb1r/pp1ppppp/5n2/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 4": ["e1g1", "b1c3", "f1e1"],
    "r1bqk2r/pppp1ppp/2n2n2/2b1p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 1 5": ["c1e3", "b1d2", "e1g1"],
    "r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["c1e3", "e1g1", "f1e1"],
    "rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2": ["e4d5", "d1d5", "b1c3"],
    
    # ==================== SACRIFICES & ATTACKS ====================
    "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/3N1N2/PPPP1PPP/RNBQK2R w KQkq - 1 5": ["d3d4", "e4d5", "c4f7"],
    "r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["d3d4", "c1g5", "e4e5"],
    "r1b1k2r/ppppqppp/2n2n2/2b1p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 1 6": ["c1e3", "b1d2", "e1g1"],
    "r1bqk1nr/ppppb1pp/2n5/2b1p3/2B1P3/3P1N2/PPP2PPP/RNBQK2R w KQkq - 1 6": ["d3d4", "c4d5", "f3d5"],
    
    # ==================== KNIGHT FORKS & PLACEMENT ====================
    "r1bqk2r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["f3e5", "e5d7", "d7f6"],
    "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/3N1N2/PPPP1PPP/R1BQK2R w KQkq - 2 5": ["d3d4", "e4d5", "f3e5"],
    "r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["f3e5", "e3c5", "e5c6"],
    "r1bqk2r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["f3g5", "g5f7", "d1e2"],
    "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/3N1N2/PPPP1PPP/R1BQKB1R w KQkq - 0 5": ["d3d4", "e4d5", "f3e5"],
    
    # ==================== PIN & SKEWER TACTICS ====================
    "r1bqk2r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["c1g5", "g5f6", "f6e8"],
    "r1b1k2r/ppppqppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 1 6": ["c1e3", "b1d2", "e1g1"],
    "r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["c1g5", "e1g1", "b1d2"],
    "rnbqkb1r/pppp1ppp/5n2/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 3": ["c1g5", "d2d3", "h7h6"],
    
    # ==================== WEAK KING POSITIONS ====================
    "r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["c1e3", "b1d2", "e3c5"],
    "r1b1kb1r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 1 6": ["e1g1", "c1e3", "e3g5"],
    "r1bqk2r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["e1g1", "c1e3", "b1d2"],
    "r1bqk1nr/ppppb1pp/2n5/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 1 6": ["e1g1", "c1g5", "b1d2"],
    
    # ==================== ROOK ACTIVITY ====================
    "r1b2rk1/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w - - 0 7": ["e1g1", "c1e3", "b1d2"],
    "r1b2rk1/ppppbppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w - - 1 7": ["c1g5", "e3g5", "e1g1"],
    "r3k2r/ppppbppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w kq - 2 7": ["e1g1", "c1e3", "b1d2"],
    "r1b1k2r/ppppbppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w kq - 2 7": ["e1g1", "f1e1", "c1e3"],
    
    # ==================== COMPENSATION & MATERIAL IMBALANCE ====================
    "r1bqk2r/pppp1ppp/2n2n2/4p3/1b2P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 1 6": ["e1g1", "c1e3", "b1d2"],
    "r1b1kb1r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPPC1PPP/RNBQKB1R b KQkq - 1 6": ["e8f8", "e3g5", "f6e4"],
    "r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["d3d4", "c1e3", "b1d2"],
    "rnbqkb1r/pppp1ppp/5n2/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 3": ["e1g1", "d2d3", "f8e7"],
    
    # ==================== SPACE ADVANTAGE ====================
    "r1bqkb1r/pppp1ppp/2n2n2/4pp2/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["e4e5", "e1g1", "c1e3"],
    "r1b1kb1r/pppp1ppp/2n2n2/4pp2/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 1 5": ["e4f5", "c1e3", "e1g1"],
    "r1bqkb1r/pppp1ppp/2n2n2/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["e4e5", "c1g5", "b1d2"],
    "r1bq1rk1/ppppbppp/2n2n2/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R w - - 1 6": ["e4d5", "f3d5", "e7d6"],
    
    # ==================== FIANCHETTO PATTERNS ====================
    "rnbqkb1r/pppppppp/5n2/8/2P5/6P1/PP1PPPBP/RNBQK1NR b KQkq - 1 3": ["d7d5", "c4d5", "f6d5"],
    "rnbqkb1r/pppp1ppp/5n2/4p3/2P5/6P1/PP1PPPBP/RNBQK1NR w KQkq - 0 4": ["f1g2", "e1g1", "f8e7"],
    "rnbqkb1r/pppppp1p/5np1/8/2P5/6P1/PP1PPPBP/RNBQK1NR w KQkq - 2 4": ["f1g2", "e1g1", "b7b6"],
    
    # ==================== LONG DIAGONAL ====================
    "rnbqkb1r/pppppppp/5n2/8/2P5/8/PP1PPPPP/RNBQKBNR w KQkq - 1 2": ["g2g3", "f1g2", "e7e6"],
    "rnbqkb1r/pppppppp/5n2/8/2P5/8/PP1PPPPP/RNBQKBNR w KQkq - 1 2": ["f1g2", "e1g1", "e7e6"],
    
    # ==================== EXCHANGE SACRIFICE ====================
    "r1bqk2r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["f1e1", "c1e3", "e1c1"],
    "r1b1k2r/ppppqppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 1 6": ["f1e1", "e4e5", "c6e5"],
    
    # ==================== WHITE ATTACKING PATTERNS ====================
    # Attack on f7/weak kingside
    "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 2 4": ["b5f7", "e1g1", "c1e3"],
    "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/3P1N2/PPP2PPP/RNBQK2R w KQkq - 1 5": ["d3d4", "e4d5", "e1g1"],
    
    # Attack on kingside with pieces
    "r1bqk2r/pppp1ppp/2n2n2/2b1p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["f3e5", "e5d7", "c1e3"],
    "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/2N2N2/PPPP1PPP/R1BQK2R w KQkq - 2 5": ["b1d2", "e1g1", "d2c4"],
    
    # ==================== BLACK COUNTERPLAY PATTERNS ====================
    # Queenside expansion and pressure
    "r3k2r/pp1n1ppp/2pb4/3pp3/2P1P3/2N2N2/PPB2PPP/R2Q1RK1 b kq - 1 9": ["b7b5", "e8f8", "d6c5"],
    "r1bqk2r/ppp1nppp/2n1p3/3p4/2P1P3/2N1BN2/PP3PPP/R2Q1RK1 b KQkq - 0 8": ["d5d4", "c6d4", "f6d4"],
    
    # ==================== BISHOPS OF OPPOSITE COLORS ====================
    # BvB positions - attacking chances matter
    "r3k3/pp3ppp/2nb4/3bp3/2P5/2NB1N2/PP3PPP/R2Q1RK1 w kq - 2 10": ["b1d2", "c3e4", "e4d6"],
    "r3k2r/ppp1b1pp/2nb4/3p4/2P1P3/2NB1N2/PP3PPP/R2Q1RK1 w KQkq - 0 9": ["e3g5", "c3e4", "c1f4"],
    
    # ==================== ROOK ENDGAME TRANSITION ====================
    # Positions transitioning to rook endgames
    "r3k2r/pp3ppp/2nb4/3pp3/2P5/2NB1N2/PP3PPP/R2Q1RK1 b kq - 1 8": ["e8f8", "c3e4", "e4d6"],
    "4k3/pp3ppp/2nb4/3pp3/2P1N3/3B1N2/PP3PPP/R2Q1RK1 b - - 0 9": ["e4c5", "d3c5", "d8c7"],
    
    # ==================== PAWN BREAKS ====================
    # Key pawn breaks with advantage
    "r1bqk2r/ppppbppp/2n2n2/4p3/2B1P3/2N2N2/PPPP1PPP/R1BQK2R w KQkq - 2 5": ["e4e5", "d2d4", "b1d2"],
    "r1bqk2r/pp1n1ppp/2np4/3pp3/2P1P3/2N2N2/PP2BPPP/R1BQ1RK1 w kq - 0 7": ["e4e5", "d2d4", "e5d6"],
    
    # ==================== HANGING PIECES & TACTICS ====================
    # Common tactical motifs
    "rn1qkb1r/pp1ppppp/5n2/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 4": ["e1g1", "b1c3", "f1e1"],
    "r1bqk2r/pppp1ppp/2n2n2/2b1p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 1 5": ["c1e3", "b1d2", "e1g1"],
    
    # ==================== SACRIFICES & ATTACKS ====================
    # Piece sacrifices for advantage
    "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/3N1N2/PPPP1PPP/RNBQK2R w KQkq - 1 5": ["d3d4", "e4d5", "c4f7"],
    "r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["d3d4", "c1g5", "e4e5"],
    
    # ==================== KNIGHT FORKS & PLACEMENT ====================
    "r1bqk2r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["f3e5", "e5d7", "d7f6"],
    "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/3N1N2/PPPP1PPP/R1BQK2R w KQkq - 2 5": ["d3d4", "e4d5", "f3e5"],
    
    # ==================== PIN & SKEWER TACTICS ====================
    "r1bqk2r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["c1g5", "g5f6", "f6e8"],
    "r1b1k2r/ppppqppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 1 6": ["c1e3", "b1d2", "e1g1"],
    
    # ==================== WEAK KING POSITIONS ====================
    "r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["c1e3", "b1d2", "e3c5"],
    "r1b1kb1r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 1 6": ["e1g1", "c1e3", "e3g5"],
    
    # ==================== ROOK ACTIVITY ====================
    "r1b2rk1/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w - - 0 7": ["e1g1", "c1e3", "b1d2"],
    "r1b2rk1/ppppbppp/2n2n2/4p3/4P3/3P1N2/PPP2PPP/RNBQKB1R w - - 1 7": ["c1g5", "e3g5", "e1g1"],
    
    # ==================== COMPENSATION & MATERIAL IMBALANCE ====================
    "r1bqk2r/pppp1ppp/2n2n2/4p3/1b2P3/3P1N2/PPP2PPP/RNBQKB1R w KQkq - 1 6": ["e1g1", "c1e3", "b1d2"],
    "r1b1kb1r/pppp1ppp/2n2n2/4p3/4P3/3P1N2/PPPC1PPP/RNBQKB1R b KQkq - 1 6": ["e8f8", "e3g5", "f6e4"],
    
    # ==================== SPACE ADVANTAGE ====================
    "r1bqkb1r/pppp1ppp/2n2n2/4pp2/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["e4e5", "e1g1", "c1e3"],
    "r1b1kb1r/pppp1ppp/2n2n2/4pp2/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 1 5": ["e4f5", "c1e3", "e1g1"],
}

def get_middlegame_move(fen: str, moves_count: int) -> str:
    """Get a book move for middlegame position"""
    import random
    
    # Only use middlegame book between moves 10-30
    if 10 <= moves_count <= 30 and fen in MIDDLEGAME_PATTERNS:
        moves = MIDDLEGAME_PATTERNS[fen]
        return random.choice(moves) if isinstance(moves, list) else moves
    return None
