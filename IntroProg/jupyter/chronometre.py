import ipywidgets
import time

from threading import Timer, Thread, Event

__version__ = "0.1"


class PerpetualTimer:
    """
    A timer
    """

    def __init__(self, fps, tick):
        """
        Initialization of the PerpetualTimer

        Parameters
        ----------
        fps: (type=int) frames per second
        tick: player's tick
        """
        self.fps = fps
        self.tick = tick
        self.thread = None  # Timer(self.t,self.handle_function)
        self.isrunning = False
        self.run()

    def handle_function(self):
        """
        Control the time: start, stop, how long to wait, cancel, restart...
        """
        assert self.thread is not None
        assert self.isrunning
        self.tick()
        self.thread.cancel()
        self.thread = Timer(1 / self.fps, self.handle_function)
        self.thread.start()

    def set_fps(self, fps):
        """
        Convert fps to second
        """
        self.fps = fps
        if self.isrunning:
            self.cancel()
            self.start()

    def run(self):
        """
        Start the timer
        """
        if self.isrunning:
            return
        self.thread = Timer(1 / self.fps, self.handle_function)
        self.thread.start()
        self.isrunning = True

    def running(self):
        """
        Return whether the timer is running or not
        """
        return self.isrunning

    def start(self):
        """
        Start the timer
        """
        if self.isrunning:
            return
        self.thread = Timer(1 / self.fps, self.handle_function)
        self.thread.start()
        self.isrunning = True

    def cancel(self):
        """
        Stop the timer
        """
        if self.isrunning:
            self.thread.cancel()
            self.thread = None
            self.isrunning = False


class ModeleChronometre:
    startTime = None
    stopTime = None

    def start(self):
        self.startTime = time.time()
        self.stopTime = None

    def stop(self):
        self.stopTime = time.time()

    def time(self):
        if self.startTime is None:
            return 0
        if self.stopTime is None:
            return time.time() - self.startTime
        return self.stopTime - self.startTime


class Chronometre(ipywidgets.HBox):
    def __init__(self):
        self.chronometre = ModeleChronometre()

        startButton = ipywidgets.Button(description="Je démarre", icon="play")
        stopButton = ipywidgets.Button(description="J'ai fini!", icon="stop")
        timeLabel = ipywidgets.Label()

        startButton.on_click(lambda event: self.start())
        stopButton.on_click(lambda event: self.stop())

        def showTime():
            timeLabel.value = f"Temps: {self.chronometre.time():.1f} s"

        self.timer = PerpetualTimer(10, showTime)

        super().__init__([startButton, stopButton, timeLabel])

    def start(self) -> None:
        self.chronometre.start()
        self.timer.start()

    def stop(self) -> None:
        self.chronometre.stop()
        self.timer.cancel()

