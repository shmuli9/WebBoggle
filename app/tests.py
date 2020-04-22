import time

from app.models import Board
from app.solver import generate_valid_words
from app.wordtree import wt


def run_generator(board):
    start = time.time()
    word_list = generate_valid_words(board)
    end = time.time()

    print(f"{len(word_list)} words were generated in {end - start:.6f} seconds")
    return sorted(word_list)


def verify_algo(strict=False):
    if not strict:
        print("\nPreconfigured board:")
        print("-" * 20)
    output = run_generator(Board("LOPGPOCIHBIEGKLS"))

    expected_output = ['BICE', 'BICES', 'BILE', 'BILES', 'BILK', 'BIO', 'BIOPIC', 'BIS', 'BISE', 'BOH', 'BOI',
                       'BOIL', 'BOILS',
                       'BOIS', 'BOLO', 'BOO', 'BOOL', 'BOP', 'CEIL', 'CEILS', 'CEL', 'CELS', 'CIBOL', 'CIEL',
                       'CIELS', 'CIG',
                       'CIS', 'COB', 'COBLE', 'COBLES', 'COIL', 'COILS', 'COL', 'COLOBI', 'COO', 'COOL', 'COOP',
                       'COP',
                       'COPIES', 'ECO', 'EIK', 'ELK', 'ELS', 'GIE', 'GIES', 'GIP', 'HOB', 'HOC', 'HOI', 'HOIK',
                       'HOIS',
                       'HOISE', 'HOLO', 'HOLP', 'HOO', 'HOOP', 'HOP', 'ICE', 'ICES', 'ILK', 'ISLE', 'KIS', 'LEI',
                       'LEIS',
                       'LES', 'LIB', 'LICE', 'LIE', 'LIES', 'LIS', 'LOB', 'LOBI', 'LOCI', 'LOCIE', 'LOCIES',
                       'LOCIS', 'LOCO',
                       'LOO', 'LOOBIES', 'LOOIE', 'LOOIES', 'LOOP', 'LOP', 'OBI', 'OBIS', 'OIK', 'OIL', 'OILS',
                       'OIS', 'OOH',
                       'OOP', 'PHO', 'PHOBIC', 'PIC', 'PICE', 'PIE', 'PIES', 'PIG', 'PLOP', 'POCO', 'POH', 'POI',
                       'POIS',
                       'POISE', 'POL', 'POLO', 'POO', 'POOH', 'POOL', 'POOP', 'POP', 'SEC', 'SECO', 'SEI', 'SEIK',
                       'SEIL',
                       'SEL', 'SIB', 'SIC', 'SICE', 'SIK', 'SILE', 'SILK', 'SLICE']

    if not strict:
        # run_generator(Board("QuEENPOCIHBIEGKLS"))

        print("\nRandom boards:")
        print("-" * 20)
        for _ in range(1):
            run_generator(Board())

    if output == expected_output:
        return True
    return False


def test_suite(num_runs=10):
    def avg(numbers):
        total = 0
        for el in numbers:
            total += el
        return total / len(numbers)

    dice = ["QuEENPOCIHBIEGKLS", "LOPGPOCIHBIEGKLS", "EDRQuHIECTSAZNLSE"]
    #  dice[0] if run % 2 == 0 else dice[1]

    run_times = []
    for run in range(num_runs):
        wt.resetTree()
        # d = dice[0] if run % 2 == 0 else dice[1]
        d = ""
        start = time.time()
        word_list = generate_valid_words(Board(d))
        end = time.time()
        del word_list
        run_times.append(end - start)
        del start, end

    precision = 6
    print(
        f"average run time over {num_runs} random boards was: {avg(run_times):.{precision}f}s (total:{sum(run_times):.{precision}f}s)")
    print(f"max run time was {max(run_times):.{precision}f}s")
    print(f"min run time was {min(run_times)}s")
    print(f"delta (max - min) run time was {max(run_times) - min(run_times):.{precision}f}s")
    print(run_times[:1000])


if not verify_algo(True):
    print("❌ - Algo failed to run successfully on Preconfigured board ")
else:
    pass
    print("Algo verified, running test suite")
    test_suite(100)


def checkWordTree(wordList, wordTree):
    print("checking wordtree")
    missed_words = []
    for word in wordList:
        if not wordTree.findString(word):
            missed_words.append(word)
    print("finished checking wordtree")
    print(len(missed_words), " words were skipped:\n", missed_words)

# checkWordTree(words, wt)
