import sys

import PySide2
from presenter.Presenter import Presenter


if __name__ == "__main__":
    app = Presenter(sys.argv)
    sys.exit(app.exec_())
