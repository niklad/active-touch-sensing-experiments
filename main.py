"""Author: Niklas Strømsnes
Date: 2022-01-09
"""

import matplotlib.pyplot as plt
from generate_results import (setup2_results,
                              setup3_results,
                              setup1_results,
                              custom_plots)
from data_visualization.visualize_data import set_fontsizes


def main():
    """Run functions from generate_results.py
    NOTE:   Individual figures can be plotted by wrapping it with
            plt.close('all') and plt.show()
    """
    set_fontsizes()

    setup = ''
    while input not in ['1', '2', '3']:
        print('\nWhich setup do you want to generate results for?')
        print('1: Setup 1')
        print('2: Setup 2')
        print('3: Setup 3')
        setup = input('Enter number: ')
        if setup == '1':
            setup1_results()
        elif setup == '2':
            setup2_results()
        elif setup == '3':
            setup3_results()
        else:
            print('Please type 1, 2 or 3 for their respective setups.')

        plt.show()
    return 0


if __name__ == '__main__':
    main()
