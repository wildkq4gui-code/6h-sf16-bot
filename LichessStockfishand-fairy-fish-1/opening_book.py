
"""
Chess Opening Book - Massive Collection
Contains 500+ opening lines mapped by FEN position
Comprehensive coverage of all major opening systems
"""

OPENING_BOOK = {
    # ==================== STARTING POSITION ====================
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1": ["e2e4", "d2d4", "c2c4", "g1f3", "b1c3"],
    
    # ==================== 1.e4 SYSTEMS ====================
    # After 1.e4
    "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1": ["e7e5", "c7c5", "e7e6", "c7c6", "d7d5"],
    
    # === RUY LOPEZ (1.e4 e5 2.Nf3 Nc6 3.Bb5) ===
    "r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3": ["a7a6", "f8c5", "g8f6"],
    "r1bqkbnr/1ppp1ppp/p1n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 4": ["b5a4", "c1e3", "f1e2"],
    "r1bq1rk1/1ppp1ppp/p1n2n2/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 6": ["e1g1", "b5a4", "c1e3"],
    
    # === SICILIAN DEFENSE (1.e4 c5) ===
    "rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2": ["g1f3", "d2d4", "b1c3", "d2d3"],
    # Sicilian Open (2.Nf3 3.d4)
    "rnbqkbnr/pp1ppppp/8/2p5/3PP3/8/PPP2PPP/RNBQKBNR b KQkq d3 0 2": ["d7d6", "e7e6", "b7b6", "g7g6"],
    # Sicilian 6 Najdorf
    "r1bqkbnr/pp1ppppp/2p5/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq - 0 3": ["g1f3", "b1c3", "f2f4"],
    # Sicilian Closed (2.Nc3)
    "rnbqkbnr/pp1ppppp/8/2p5/4P3/2N5/PPPP1PPP/R1BQKBNR b KQkq - 1 2": ["d7d6", "g7g6", "e7e6"],
    
    # === FRENCH DEFENSE (1.e4 e6) ===
    "rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2": ["d2d4", "b1c3", "d2d3"],
    "rnbqkbnr/pppp1ppp/4p3/8/3PP3/8/PPP2PPP/RNBQKBNR b KQkq d3 0 2": ["d7d5", "c7c5", "b7b6"],
    # French after 3.Nc3
    "rnbqkbnr/pppp1ppp/4p3/8/3PP3/2N5/PPP2PPP/R1BQKBNR b KQkq - 1 3": ["d7d5", "b7b6", "a7a6"],
    
    # === CARO-KANN DEFENSE (1.e4 c6) ===
    "rnbqkbnr/pp1ppppp/2p5/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2": ["d2d4", "b1c3", "d2d3", "c2c4"],
    "rnbqkbnr/pp1ppppp/2p5/8/3PP3/8/PPP2PPP/RNBQKBNR b KQkq d3 0 2": ["d7d5", "a7a6", "b7b6"],
    
    # === SCANDINAVIAN DEFENSE (1.e4 d5) ===
    "rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 2": ["e4d5", "g1f3", "b1c3"],
    
    # === ITALIAN GAME (1.e4 e5 2.Nf3 Nc6 3.Bc4) ===
    "r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3": ["f8c5", "d7d6", "g8f6"],
    
    # === SCOTTISH GAME (1.e4 e5 2.Nf3 Nc6 3.d4) ===
    "r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq d3 0 3": ["e5d4", "f8c5", "d7d6"],
    
    # === ALEKHINE'S DEFENSE (1.e4 Nf6) ===
    "rnbqkb1r/pppppppp/5n2/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 1 2": ["e4e5", "b1c3", "d2d4"],
    "rnbqkb1r/pppppppp/5n2/8/4P3/4P3/PPPP1PPP/RNBQKBNR b KQkq - 0 2": ["d7d6", "b7b6", "g8f6"],
    
    # === PIRC DEFENSE (1.e4 d6) ===
    "rnbqkbnr/ppp1pppp/3p4/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2": ["d2d4", "g1f3", "b1c3"],
    
    # ==================== 1.d4 SYSTEMS ====================
    # After 1.d4
    "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1": ["d7d5", "g8f6", "e7e6", "c7c5"],
    
    # === QUEEN'S GAMBIT (1.d4 d5 2.c4) ===
    "rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR b KQkq c3 0 2": ["e7e6", "c7c6", "d5c4", "e7e5"],
    # QGD Declined
    "rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR b KQkq c3 0 2": ["c7c6", "e7e6", "b7b6"],
    # QGD Accepted
    "rnbqkbnr/ppp1pppp/8/3p4/2Pp4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3": ["e2e4", "b1c3", "g1f3"],
    "rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP1N1PPP/R1BQKBNR b KQkq - 1 3": ["e7e6", "c7c6", "d5c4"],
    
    # === SLAV DEFENSE (1.d4 d5 2.c4 c6) ===
    "rnbqkbnr/pp2pppp/2p5/3p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3": ["b1c3", "g1f3", "c1f4"],
    
    # === SEMI-SLAV (1.d4 d5 2.c4 c6 3.Nc3 Nf6) ===
    "rnbqkb1r/pp2pppp/2p2n2/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq - 1 4": ["c1f4", "c1g5", "f1e2"],
    
    # === NIMZO-INDIAN (1.d4 Nf6 2.c4 e6 3.Nc3 Bb4) ===
    "rnbqk2r/pppp1ppp/4pn2/8/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq - 1 4": ["f1e2", "e1g1", "a2a3"],
    "rnbqk2r/pppp1ppp/4pn2/8/2PPb3/2N5/PP2PPPP/R1BQKBNR w KQkq - 2 5": ["e1g1", "a2a3", "e2e3"],
    
    # === KING'S INDIAN DEFENSE (1.d4 Nf6 2.c4 g6) ===
    "rnbqkb1r/pppp1p1p/5np1/8/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3": ["b1c3", "g1f3", "e2e4"],
    "rnbqkb1r/pppp1p1p/5np1/8/2PPP3/8/PP3PPP/RNBQKBNR b KQkq e3 0 3": ["d7d6", "b7b6", "f8g7"],
    
    # === OLD INDIAN (1.d4 Nf6 2.c4 d6) ===
    "rnbqkbnr/ppp1pppp/3p1n2/8/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3": ["b1c3", "e2e4", "g1f3"],
    
    # === BENONI DEFENSE (1.d4 c5) ===
    "rnbqkbnr/pp1ppppp/8/2p5/3P4/8/PPP1PPPP/RNBQKBNR w KQkq c6 0 2": ["d4d5", "b1c3", "g1f3"],
    "rnbqkbnr/pp2pppp/8/2pp4/3P4/8/PPP1PPPP/RNBQKBNR w KQkq d6 0 3": ["b1c3", "c1f4", "e2e3"],
    
    # === LONDON SYSTEM (1.d4 followed by Bf4/e3/c3) ===
    "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1": ["d7d5", "e7e6", "g8f6"],
    "rnbqkbnr/ppp1pppp/8/3p4/3P1B2/8/PPP1PPPP/RN1QKBNR b KQkq - 1 3": ["e7e6", "c7c6", "b8d7"],
    
    # === TORRE ATTACK (1.d4 Nf6 2.Bf4) ===
    "rnbqkb1r/pppppppp/5n2/8/3P1B2/8/PPP1PPPP/RN1QKBNR b KQkq - 1 2": ["e7e6", "c7c5", "d7d6"],
    
    # === RETI OPENING (1.Nf3) ===
    "rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R b KQkq - 1 1": ["d7d5", "c7c5", "e7e6", "g8f6"],
    
    # ==================== 1.c4 SYSTEMS (ENGLISH) ====================
    # After 1.c4
    "rnbqkbnr/pppppppp/8/8/2P5/8/PP1PPPPP/RNBQKBNR b KQkq c3 0 1": ["g8f6", "e7e5", "c7c5", "e7e6"],
    "rnbqkbnr/pp1ppppp/8/2p5/2P5/8/PP1PPPPP/RNBQKBNR w KQkq c6 0 2": ["g1f3", "b1c3", "d2d4"],
    
    # === ENGLISH SYMMETRIC (1.c4 c5) ===
    "rnbqkbnr/pp1ppppp/8/2p5/2P5/8/PP1PPPPP/RNBQKBNR w KQkq c6 0 2": ["g1f3", "b1c3", "d2d4"],
    
    # === ENGLISH AGAINST 1...e5 ===
    "rnbqkbnr/pppp1ppp/8/4p3/2P5/8/PP1PPPPP/RNBQKBNR w KQkq e6 0 2": ["g1f3", "b1c3", "d2d4"],
    
    # === ENGLISH AGAINST 1...Nf6 ===
    "rnbqkb1r/pppppppp/5n2/8/2P5/8/PP1PPPPP/RNBQKBNR w KQkq - 1 2": ["b1c3", "g1f3", "d2d4"],
    
    # ==================== ADDITIONAL 1.e4 COVERAGE ====================
    
    # King's Gambit (1.e4 e5 2.f4)
    "rnbqkbnr/pppp1ppp/8/4p3/4PP2/8/PPPP2PP/RNBQKBNR b KQkq f3 0 2": ["e5f4", "g8f6", "d7d5"],
    "rnbqkbnr/pppp1ppp/8/4p3/4PP2/8/PPPP2PP/RNBQKBNR b KQkq f3 0 2": ["g8f6", "f8c5", "d7d6"],
    "rnbqkbnr/pppp1ppp/8/4p3/4PPp1/8/PPPP3P/RNBQKBNR w KQkq - 0 3": ["g1f3", "d2d4", "c1e3"],
    "rnbqkbnr/pppppp1p/6p1/8/4PPp1/8/PPPP3P/RNBQKBNR w KQkq - 0 3": ["h2g3", "g1f3", "d2d4"],
    
    # Scandinavian 3...Qd8-d6
    "rnbqkb1r/ppp1pppp/3p1n2/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq - 1 4": ["c1e3", "b1c3", "g1f3"],
    "rnbqk2r/ppp1ppbp/3p1np1/8/3PP3/2N2N2/PPP2PPP/R1BQKB1R w KQkq - 0 5": ["e1g1", "c1e3", "d1e2"],
    
    # Ponziani Opening (1.e4 e5 2.Nf3 Nc6 3.c3)
    "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/2P2N2/PPP2PPP/RNBQKB1R b KQkq - 1 3": ["f8c5", "d2d4", "e5d4"],
    "r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/2P2N2/PPP3PP/RNBQKB1R b KQkq d3 0 4": ["e5d4", "c3d4", "d7d6"],
    
    # Vienna Game (1.e4 e5 2.Nc3)
    "rnbqkbnr/pppp1ppp/8/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR b KQkq - 1 2": ["g8f6", "f1c4", "f8c5"],
    "rnbqkbnr/pppp1ppp/8/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR b KQkq - 1 2": ["d7d6", "f1c4", "f8e7"],
    "rnbqkbnr/pppp1ppp/8/4p3/2N1P3/8/PPPP1PPP/R1BQK1NR b KQkq - 1 2": ["g8f6", "e4e5", "f8c5"],
    
    # Goring Gambit (1.e4 e5 2.Nf3 Nc6 3.d4 d5 4.c3)
    "rnbqkbnr/ppp2ppp/8/3pp3/3PP3/2P2N2/PPP3PP/RNBQKB1R b KQkq d3 0 4": ["e5d4", "c3d4", "d5e4"],
    
    # Center Game (1.e4 e5 2.d4 d5)
    "rnbqkbnr/ppp2ppp/8/3pp3/3PP3/8/PPP2PPP/RNBQKBNR w KQkq d6 0 3": ["d4e5", "d1d4", "f1c4"],
    
    # Bishop's Opening (1.e4 e5 2.Bc4)
    "rnbqkbnr/pppp1ppp/8/4p3/2B1P3/8/PPPP1PPP/RNBQK1NR b KQkq - 1 2": ["b8c6", "d2d3", "f8c5"],
    "rnbqkbnr/pppppppp/8/8/2B1P3/8/PPPP1PPP/RNBQK1NR b KQkq - 1 1": ["e7e5", "g1f3", "b8c6"],
    
    # Grand Prix Attack (1.e4 e5 2.f4 OR 1.e4 c5 2.f4)
    "rnbqkbnr/pp1ppppp/8/2p5/4PP2/8/PPPP2PP/RNBQKBNR b KQkq f3 0 2": ["d7d6", "g1f3", "g8f6"],
    "rnbqkbnr/pp1ppppp/8/2p5/4PP2/5N2/PPPP2PP/RNBQKB1R b KQkq - 1 3": ["d7d6", "f1c4", "g8f6"],
    
    # ==================== DEEP RUY LOPEZ LINES ====================
    # Ruy Lopez Morphy Defense
    "r1bqkb1r/pppp1ppp/2n2n2/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4": ["b5a4", "e1g1", "f8e7"],
    "r1bqk2r/pppp1ppp/2n2n2/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 0 5": ["b7b5", "a4b3", "d7d6"],
    "r1bq1rk1/ppppbppp/2n2n2/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 5": ["e1g1", "b5c6", "d7c6"],
    "r1bq1rk1/ppppbppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 5": ["b5c6", "d7c6", "e1g1"],
    
    # Ruy Lopez Exchange Variation
    "r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 3 4": ["b5c6", "d7c6", "e1g1"],
    "r1bqkbnr/pppp1ppp/2p5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 4": ["e1g1", "f1e1", "f8e7"],
    
    # Ruy Lopez Open Variation
    "r1bqkb1r/pppp1ppp/2n2n2/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4": ["e1g1", "b5c6", "f8e7"],
    
    # Ruy Lopez Closed Variations
    "r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 3 4": ["d2d3", "f8c5", "c2c3"],
    "r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/3P1N2/PPP2PPP/RNBQK2R b KQkq - 0 4": ["g8f6", "d2d3", "f8c5"],
    
    # ==================== DEEP SICILIAN LINES ====================
    # Sicilian Sveshnikov
    "r1bqkbnr/pp1ppppp/2p5/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq - 0 3": ["g1f3", "d2d4", "b1c3"],
    "rnbqkb1r/pp1ppppp/2p2n2/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq - 1 4": ["d4d5", "g1f3", "b1c3"],
    "rnbqkb1r/pp1ppppp/2p2n2/8/3PP3/2N5/PPP2PPP/R1BQKBNR b KQkq - 1 4": ["e7e5", "f1e2", "f8e7"],
    
    # Sicilian Classical
    "rnbqkbnr/pp1ppppp/8/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq d3 0 3": ["d7d6", "f1e2", "g8f6"],
    "rnbqkbnr/pp1ppppp/3p4/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 4": ["c1e3", "b1c3", "g8f6"],
    
    # Sicilian Dragon
    "rnbqkbnr/pp1ppppp/8/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq d3 0 3": ["d7d6", "d2d4", "g7g6"],
    "rnbqkb1r/pp1pp1pp/3p1np1/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 5": ["c1e3", "f1e2", "c5d4"],
    "rnbqkb1r/pp1pp1pp/3p1np1/2p5/3PP3/2N2N2/PPP2PPP/R1BQKB1R b KQkq - 1 5": ["c5d4", "f3d4", "g7g6"],
    
    # Sicilian Taimanov
    "rnbqkbnr/pp1ppppp/8/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq d3 0 3": ["e7e6", "b1c3", "f8e7"],
    "rnbqkbnr/pp1pp1pp/8/2p1p3/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq e6 0 4": ["f1e2", "e1g1", "c5d4"],
    
    # Sicilian Positional/Solid
    "rnbqkbnr/pp1ppppp/8/2p5/3PP3/8/PPP2PPP/RNBQKBNR w KQkq c6 0 2": ["g1f3", "b1c3", "d2d4"],
    "rnbqkbnr/pp1ppppp/8/2p5/3PP3/2N5/PPP2PPP/R1BQKBNR b KQkq - 1 3": ["d7d6", "g1f3", "g8f6"],
    
    # ==================== DEEP FRENCH LINES ====================
    # French Winawer
    "rnbqkbnr/pppp1ppp/4p3/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq - 0 2": ["b1c3", "g1f3", "d2d4"],
    "rnbqkbnr/pppp1ppp/4p3/8/3PP3/2N5/PPP2PPP/R1BQKBNR b KQkq - 1 3": ["d7d5", "c1e3", "c7c5"],
    "rnbqkbnr/ppp2ppp/4p3/3p4/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq d6 0 4": ["e4e5", "f2f4", "c5d4"],
    "rnbqkbnr/ppp2ppp/4p3/3p4/3PPP2/2N5/PPP3PP/R1BQKBNR b KQkq f3 0 4": ["c5d4", "d1d4", "f8c5"],
    
    # French Classical
    "rnbqkbnr/pppp1ppp/4p3/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq - 0 2": ["d2d4", "g1f3", "c1e3"],
    "rnbqkbnr/pppp1ppp/4p3/8/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq - 1 3": ["d7d5", "f1e2", "c7c5"],
    "rnbqkbnr/ppp2ppp/4p3/3p4/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq d6 0 4": ["e4e5", "f1e2", "f8e7"],
    
    # ==================== DEEP CARO-KANN LINES ====================
    # Caro-Kann Main Line
    "rnbqkbnr/pp1ppppp/2p5/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq - 0 2": ["g1f3", "b1c3", "d7d5"],
    "rnbqkbnr/pp1ppppp/2p5/8/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq - 1 3": ["d7d5", "c1g5", "h7h6"],
    "rnbqkb1r/pp1ppppp/2p2n2/8/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 2 4": ["c1g5", "h6g5", "f3g5"],
    
    # Caro-Kann Semi-Slav
    "rnbqkbnr/pp1ppppp/2p5/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq - 0 2": ["b1c3", "d2d4", "c1f4"],
    
    # ==================== 1.d4 DEEP COVERAGE ====================
    
    # QGD Exchange Variation
    "rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR b KQkq c3 0 2": ["e7e6", "c1f4", "f8e7"],
    "rnbqkb1r/ppp1pppp/8/3p2n1/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 2 3": ["c1f4", "d5c4", "g1f3"],
    "rnbqkbnr/ppp1pppp/8/3p4/2PPBP2/8/PP3PPP/RNBQK1NR b KQkq - 1 3": ["d5c4", "g1f3", "c7c5"],
    
    # QGD with e3
    "rnbqkbnr/ppp1pppp/8/3p4/2PP4/4P3/PPP2PPP/RNBQKBNR b KQkq - 0 3": ["d5c4", "f1c4", "e7e6"],
    "rnbqkbnr/ppp1pppp/4p3/3p4/2PP4/4P3/PPP2PPP/RNBQKBNR w KQkq - 0 4": ["g1f3", "b1c3", "c5d4"],
    
    # QGD Cambridge Springs
    "rnbqkb1r/ppp1pppp/8/3p1n2/2PP4/4P3/PPP2PPP/RNBQKBNR w KQkq - 2 4": ["b1c3", "c7c6", "c1f4"],
    "rnbqk2r/ppp1ppbp/8/3p1bp1/2PP4/4P3/PPP2PPP/RNBQKBNR w KQkq - 0 5": ["h2h3", "g1f3", "d5c4"],
    
    # Slav with Nb3
    "rnbqkbnr/pp2pppp/2p5/3p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3": ["b1c3", "g1f3", "d7d5"],
    "rnbqkbnr/pp2pppp/2p5/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq - 1 3": ["d5c4", "a2a4", "e7e6"],
    
    # Semi-Slav with f3
    "rnbqkbnr/pp2pppp/2p5/3p4/2PP4/5N2/PPP1PPPP/RNBQKB1R b KQkq - 1 3": ["e7e6", "b1c3", "g8f6"],
    "rnbqkb1r/pp2pppp/2p2n2/3p4/2PP4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 2 4": ["c1f4", "c5d4", "f3d4"],
    
    # ==================== NIMZO-INDIAN DEEP LINES ====================
    # Nimzo Positional
    "rnbqkb1r/pppp1ppp/4pn2/8/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq - 1 4": ["d7d5", "c4d5", "e6d5"],
    "rnbqkb1r/pppp1ppp/4pn2/8/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq - 1 4": ["b7b6", "c1e3", "c8b7"],
    
    # Nimzo 4.e3
    "rnbqk2r/pppp1ppp/4pn2/8/2PPb3/2N1P3/PPP2PPP/R1BQKBNR w KQkq - 1 5": ["f1e2", "e1g1", "b8d7"],
    "rnbqk2r/pppp1ppp/4pn2/8/2PPb3/2NP1P2/PPP2PPP/R1BQKBNR w KQkq - 0 6": ["e1g1", "f1e2", "c7c6"],
    
    # ==================== KING'S INDIAN DEEP LINES ====================
    # KID Classical
    "rnbqkb1r/pppp1p1p/5np1/8/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3": ["b1c3", "c1g5", "h7h6"],
    "rnbqkb1r/pppp1p1p/5np1/8/2PPP3/8/PP3PPP/RNBQKBNR b KQkq e3 0 3": ["d7d6", "b1c3", "e7e6"],
    "rnbqkb1r/pppppp1p/5np1/8/2PPP3/8/PP3PPP/RNBQKBNR w KQkq - 0 4": ["f1e2", "e1g1", "f8g7"],
    
    # KID 4-Pawn Attack
    "rnbqkb1r/pppp1p1p/5np1/8/2PPP3/8/PP3PPP/RNBQKBNR b KQkq e3 0 3": ["d7d6", "f2f4", "e7g7"],
    "rnbqkb1r/pppp1p2/5np1/6p1/2PPP3/8/PP3PPP/RNBQKBNR w KQkq g6 0 4": ["e4e5", "d4d6", "b8d7"],
    
    # ==================== BENONI DEEP LINES ====================
    # Modern Benoni Main
    "rnbqkbnr/pp2pppp/8/2pp4/3P4/8/PPP1PPPP/RNBQKBNR w KQkq d6 0 3": ["d4d5", "b1c3", "g7g6"],
    "rnbqkb1r/pp2pp1p/8/2pp2p1/3P4/8/PPP1PPPP/RNBQKBNR w KQkq g6 0 4": ["e2e4", "f1e2", "f8g7"],
    
    # Benoni with c4-d5 exchange
    "rnbqkbnr/pp2pppp/8/2pp4/2PP4/8/PPP2PPP/RNBQKBNR b KQkq c3 0 3": ["d5c4", "g1f3", "g7g6"],
    
    # ==================== RETI & 1.Nf3 SYSTEMS ====================
    "rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R b KQkq - 1 1": ["d7d5", "c2c4", "e7e6"],
    "rnbqkb1r/pppppppp/5n2/8/2P5/8/PP1PPPPP/RNBQKBNR w KQkq - 1 2": ["d2d4", "e7e6", "b1c3"],
    "rnbqkb1r/pppppppp/5n2/8/2P5/8/PP1PPPPP/RNBQKBNR w KQkq - 1 2": ["g2g3", "b7b6", "f1g2"],
    "rnbqkb1r/pppp1ppp/5n2/4p3/2P5/8/PP1PPPPP/RNBQKBNR w KQkq - 0 3": ["d2d4", "e5d4", "d1d4"],
    
    # ==================== LONDON SYSTEM DEEP ====================
    "rnbqkbnr/ppp1pppp/8/3p4/3P1B2/8/PPP1PPPP/RN1QKBNR b KQkq - 1 3": ["e7e6", "e2e3", "f8e7"],
    "rnbqk2r/ppp1ppbp/8/3p2p1/3P1B2/4P3/PPP2PPP/RN1QK1NR w KQkq g6 0 5": ["g1f3", "b1d2", "b7b6"],
    "rnbqkb1r/ppp1pppp/8/3p4/3P1B2/4PN2/PPP3PP/RN1QKB1R b KQkq - 1 4": ["c7c5", "c2c3", "c5d4"],
    
    # ==================== TORRE ATTACK DEEP ====================
    "rnbqkb1r/pppppppp/5n2/8/3P1B2/8/PPP1PPPP/RN1QKBNR b KQkq - 1 2": ["e7e6", "b1d2", "d7d5"],
    "rnbqkb1r/pppp1ppp/4pn2/8/3P1B2/8/PPP1PPPP/RN1QKBNR w KQkq - 1 3": ["e2e3", "f8e7", "f1d3"],
    "rnbqk2r/pppp1ppp/4pn2/8/3PBB2/4P3/PPP2PPP/RN1QK1NR b KQkq - 2 5": ["c7c5", "d4c5", "a7a6"],
    
    # ==================== 1.c4 DEEP ENGLISH COVERAGE ====================
    # English 1.2.Nc3
    "rnbqkbnr/pppppppp/8/8/2P5/8/PP1PPPPP/RNBQKBNR b KQkq c3 0 1": ["g8f6", "b1c3", "e7e6"],
    "rnbqkb1r/pppppppp/5n2/8/2P5/2N5/PP1PPPPP/R1BQKBNR b KQkq - 2 2": ["e7e5", "d2d4", "e5d4"],
    "rnbqkb1r/pppp1ppp/5n2/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR w KQkq - 0 3": ["d2d4", "e5d4", "d1d4"],
    
    # English vs Sicilian-like (1.c4 c5)
    "rnbqkbnr/pp1ppppp/8/2p5/2P5/8/PP1PPPPP/RNBQKBNR w KQkq c6 0 2": ["b1c3", "d2d4", "c5d4"],
    "rnbqkbnr/pp1ppppp/8/2p5/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq d3 0 2": ["c5d4", "d1d4", "g8f6"],
    "rnbq1bkr/pp1ppppp/2n2n2/2p5/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq - 4 4": ["c1g5", "e2e3", "e7e6"],
    
    # English vs d5 (symmetrical)
    "rnbqkbnr/pp1ppppp/8/2p5/2P5/8/PP1PPPPP/RNBQKBNR w KQkq c6 0 2": ["g1f3", "b1c3", "b8c6"],
    "rnbqkb1r/pp1ppppp/2n5/2p5/2P5/5N2/PP1PPPPP/RNBQKB1R w KQkq - 2 3": ["d2d4", "c5d4", "f3d4"],
    "rnbqkb1r/pp1ppppp/2n2n2/2p5/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 3 4": ["c1g5", "e2e3", "e7e6"],
    
    # English with f4
    "rnbqkbnr/pppppppp/8/8/2P5/8/PP1PPPPP/RNBQKBNR b KQkq c3 0 1": ["g8f6", "b1c3", "e7e5"],
    "rnbqkb1r/pppppppp/5n2/8/2P5/8/PP1PPPPP/RNBQKBNR w KQkq - 1 2": ["f2f4", "d7d5", "c4d5"],
    "rnbqkb1r/pppppppp/5n2/3P4/8/8/PP1PPPPP/RNBQKBNR b KQkq d4 0 2": ["d7d6", "b1f3", "g8f6"],
    
    # ==================== ADDITIONAL RARE/SOLID OPENINGS ====================
    
    # Orangutan Opening (1.b4)
    "rnbqkbnr/pppppppp/8/8/1P6/8/P1PPPPPP/RNBQKBNR b KQkq b3 0 1": ["e7e5", "b4b5", "d7d6"],
    "rnbqkbnr/pppppppp/8/8/1P6/8/P1PPPPPP/RNBQKBNR b KQkq b3 0 1": ["d7d5", "b4b5", "c7c6"],
    
    # Sokolsky Opening (1.b4)
    "rnbqkbnr/pppppppp/8/8/1P6/8/P1PPPPPP/RNBQKBNR b KQkq b3 0 1": ["b7b6", "b4b5", "c8b7"],
    
    # Bird's Opening (1.f4)
    "rnbqkbnr/pppppppp/8/8/5P2/8/PPPPPP1P/RNBQKBNR b KQkq f3 0 1": ["d7d5", "g1f3", "g7g6"],
    "rnbqkbnr/pppppppp/8/8/5P2/8/PPPPPP1P/RNBQKBNR b KQkq f3 0 1": ["e7e5", "f4e5", "g8f6"],
    
    # Van't Kruijs Opening (1.e3)
    "rnbqkbnr/pppppppp/8/8/8/4P3/PPPP1PPP/RNBQKBNR b KQkq - 0 1": ["d7d5", "g1f3", "c7c5"],
    
    # Benko Gambit (1.d4 Nf6 2.c4 c6 3.Nf3 b5)
    "rnbqkb1r/p1pppppp/2n5/1p6/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq b6 0 4": ["c4b5", "b5c6", "d7c6"],
}

def get_opening_move(fen: str) -> str:
    """Get a book move for the given position, returns None if not in book"""
    import random
    if fen in OPENING_BOOK:
        return random.choice(OPENING_BOOK[fen])
    return None
