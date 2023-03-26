#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install PyQt5


# In[1]:


from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create input labels
        self.b_label = QLabel('b:', self)
        self.b_label.move(50, 50)
        self.r_label = QLabel('r:', self)
        self.r_label.move(50, 80)
        self.L_label = QLabel('L:', self)
        self.L_label.move(50, 110)
        self.fc_label = QLabel('fc:', self)
        self.fc_label.move(50, 140)
        self.fy_label = QLabel('fy:', self)
        self.fy_label.move(50, 170)
        self.K_label = QLabel('K:', self)
        self.K_label.move(50, 200)
        self.C_label = QLabel('C:', self)
        self.C_label.move(50, 230)
        self.ex_label = QLabel('ex:', self)
        self.ex_label.move(50, 260)
        self.ey_label = QLabel('ey:', self)
        self.ey_label.move(50, 290)
        self.P_label = QLabel('P:', self)
        self.P_label.move(50, 320)

        # Create input boxes
        self.b_input = QLineEdit(self)
        self.b_input.move(100, 50)
        self.r_input = QLineEdit(self)
        self.r_input.move(100, 80)
        self.L_input = QLineEdit(self)
        self.L_input.move(100, 110)
        self.fc_input = QLineEdit(self)
        self.fc_input.move(100, 140)
        self.fy_input = QLineEdit(self)
        self.fy_input.move(100, 170)
        self.K_input = QLineEdit(self)
        self.K_input.move(100, 200)
        self.C_input = QLineEdit(self)
        self.C_input.move(100, 230)
        self.ex_input = QLineEdit(self)
        self.ex_input.move(100, 260)
        self.ey_input = QLineEdit(self)
        self.ey_input.move(100, 290)
        self.P_input = QLineEdit(self)
        self.P_input.move(100, 320)

        # Create output label
        self.R_label = QLabel('R:', self)
        self.R_label.move(50, 380)

        # Create calculate button
        self.calculate_button = QPushButton('Calculate', self)
        self.calculate_button.move(100, 410)
        self.calculate_button.clicked.connect(self.calculate_R)

    def calculate_R(self):
        b = float(self.b_input.text())
        r = float(self.r_input.text())
        L = float(self.L_input.text())
        fc = float(self.fc_input.text())
        fy = float(self.fy_input.text())
        K = float(self.K_input.text())
        C = float(self.C_input.text())
        ex = float(self.ex_input.text())
        ey = float(self.ey_input.text())
        P = float(self.P_input.text())

        R = (0.53*b) + (0.15*r) + (-14.6*L) + (0.92*fc) + (0.21*fy) + (-231.9*K) + (3.47*C) + (-0.37*ex) + (-0.10*ey) + (-0.03*P)

        self.R_label.setText(f"R: {round(R, 2)}")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
  

