import argparse

import numpy as np

from handwriting.demo import Hand

SIZE_DEFAULT = -1


def get_arguments():
    parser = argparse.ArgumentParser(
        description='Text to handwriting generator.'
    )
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        '-f', '--file', help='text file to generate handwriting from')
    group.add_argument(
        '-t', '--text', help='text to generate handwriting from')
    parser.add_argument(
        '-s', '--style', help='handwriting style from 0 to 12',
        type=int, default=5)
    parser.add_argument(
        '-b', '--bias', help='handwriting bias from 0.1 to 1',
        type=float, default=0)
    parser.add_argument(
        '-c', '--color', help='add custom RGB color values to generated text',
        type=str, default='0,0,0')
    parser.add_argument(
        '-sp', '--save_path', help='specify the path to save the resulting image',
        type=str, default='images/0.png'
    )
    parser.add_argument(
        '-l', '--line_width', help='specify line width of strokes, [0.5, 2.5]',
        type=float, default=0.75
    )
    parser.add_argument(
        '-lh', '--line_height', help='specify line height',
        type=float, default=60
    )
    parser.add_argument(
        '-o', '--offset', help='offset parameter',
        type=int, default=1
    )
    parser.add_argument(
        '-w', '--width', help='size of the image, (width, height)',
        type=int, default=SIZE_DEFAULT
    )
    parser.add_argument(
        '-he', '--height', help='size of the image, (width, height)',
        type=int, default=SIZE_DEFAULT
    )

    return parser.parse_args()


if __name__ == "__main__":
    hand = Hand()
    args = get_arguments()

    if args.file:
        with open(args.file, 'r') as fl:
            lines = [i.strip() for i in fl.readlines()]
    elif args.text:
        lines = args.text.split("\\n")

    style = args.style
    bias = args.bias
    line_width = args.line_width
    line_height = args.line_height

    width = args.width
    height = args.height

    offset_param=args.offset

    color = args.color
    color = color.replace(' ', '')
    color = 'rgb(%s)' % color

    save_path = args.save_path

    if bias == 0:
        biases = .2 * np.flip(np.cumsum([len(i) == 0 for i in lines]), 0)
    else:
        biases = [bias] * len(lines)

    if not 0 <= style <= 12:
        styles = np.cumsum(np.array([len(i) for i in lines]) == 0).astype(int)
    else:
        styles = [style] * len(lines)

    stroke_colors = [color] * len(lines)
    stroke_widths = [line_width] * len(lines)
    hand.write(
        filename=save_path,
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_colors=stroke_colors,
        stroke_widths=stroke_widths,
        line_height=line_height,
        offset_param=offset_param
    )
