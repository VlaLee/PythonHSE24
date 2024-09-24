import argparse

from accessify import private


class Functional:

    def __init__(self, arguments: list):
        self.__arguments = arguments

    # polynomial(w, x) = (w1 + w2 * x2 + w3 * x3 + w4 * x4...) * regular_ratio
    @private
    def linearFunction(self, weights: list) -> float:
        regular_ratio: float = 0.00044701
        result: float = 0.0
        for i in range(len(self.__arguments)):
            result += weights[i] * self.__arguments[i]

        return result * regular_ratio

    @private
    def targetFunction(self) -> float:
        regular_ratio: float = 0.000993
        result: float = 0.0
        for arg in self.__arguments:
            result += arg

        return result * regular_ratio

    def lossFunction(self, weights: list) -> float:
        if len(weights) != len(self.__arguments):
            raise RuntimeError("weights and arguments have different sizes")

        lost: float = (
            self.targetFunction() - self.linearFunction(weights)
        ) ** 2

        return lost


parser = argparse.ArgumentParser(
    prog="WEIGHTS QUALITY TEST",
    description="Program for detecting the best weights for polynomial function"
    " which would be compared to the target function",
    allow_abbrev=False,
)

parser.add_argument(
    "-r",
    "--read",
    required=True,
    help="Choose the file to read",
    type=argparse.FileType("r"),
)

parser.add_argument(
    "-w",
    "--write",
    required=True,
    help="Choose the file to write",
    type=argparse.FileType("w"),
)

parser.add_argument(
    "-s",
    "--sorted",
    choices=["true", "false"],
    default="false",
    help="Choose 'true' if you want to sort weights from the best to the worst",
)

args = parser.parse_args()

x: list = [
    599.21870,
    -156.80855,
    607.63512,
    324.03304,
    -69.78820,
    -416.41341,
    -394.73762,
    86.22826,
    131.80216,
    405.17036,
    -271.87717,
    743.60328,
    529.15269,
    330.54512,
    61.75946,
    465.30571,
    810.95501,
    62.21053,
    913.77201,
    -584.09875,
]

fnc: Functional = Functional(x)
rowNumber: int = 1
lostFncResults: list = []

while True:
    line = args.read.readline()

    if not line:
        break

    weights: list = [float(x) for x in line.split(" ")]
    lostFncLocalResult: float = fnc.lossFunction(weights)

    lostFncResults.append((lostFncLocalResult, rowNumber))

    rowNumber += 1

if args.sorted == "true":
    lostFncResults.sort(key=lambda pair: pair[0])

for lostFncLocalResult, i in lostFncResults:
    args.write.write(
        f"Weights #{i} lost function result: {lostFncLocalResult}\n"
    )
