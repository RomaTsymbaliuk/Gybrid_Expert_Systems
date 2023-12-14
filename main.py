import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
features = ['Printer age', 'Printer mark', 'Target']
class Node:
    def __init__(self, feature_ind=None, threshold=None, left=None, right=None, info_gain=None, value=None):
        self.feature_ind = feature_ind
        self.threshold = threshold
        self.left = left
        self.right = right
        self.info_gain = info_gain
        self.value = value

class TreeDecision:
    def __init__(self, min_samples_split = 2, max_depth = 3):
        self.root = None
        self.min_samples_spit = min_samples_split
        self.max_depth = max_depth

    def build_tree(self, dataset, curr_depth=1):
        X, Y = dataset[:, :-1], dataset[ :, -1]
        num_samples, num_features = np.shape(X)
        if num_samples >= self.min_samples_spit and curr_depth <= self.max_depth:
            best_split = self.get_best_split(dataset, num_samples, num_features)
            if best_split["info_gain"] > 0:
                left_subt = self.build_tree(best_split["dataset_left"], curr_depth + 1)
                right_subt = self.build_tree(best_split["dataset_right"], curr_depth + 1)
                return Node(best_split["feature_index"], best_split["threshold"],
                            left_subt, right_subt, best_split["info_gain"])
        leaf_val = self.calculate_leaf_val(Y)

        return Node(value=leaf_val)

    def get_best_split(self, dataset, num_samples, num_features):
        best_split = {}
        max_info_gain = -float("inf")

        for feature_index in range(num_features):
            feature_val = dataset[:, feature_index]
            possible_thresholds = np.unique(feature_val)
            for threshold in possible_thresholds:
                dataset_left, dataset_right = self.split(dataset, feature_index, threshold)
                if len(dataset_left) > 0 and len(dataset_right) > 0:
                    y, left_y, right_y = dataset[:, -1], dataset_left[:, -1], dataset_right[:, -1]
                    curr_info_gain = self.information_gain(y, left_y, right_y, "entropy")
                    if curr_info_gain > max_info_gain:
                        best_split["feature_index"] = feature_index
                        best_split["threshold"] = threshold
                        best_split["dataset_left"] = dataset_left
                        best_split["dataset_right"] = dataset_right
                        best_split["info_gain"] = curr_info_gain
                        max_info_gain = curr_info_gain
        return best_split
    def split(self, dataset, feature_ind, threshold):
 #       print(dataset)
        dataset_left = np.array([row for row in dataset if row[feature_ind] <= threshold])
        dataset_right = np.array([row for row in dataset if row[feature_ind] > threshold])
        return dataset_left, dataset_right

    def information_gain(self, parent, l_ch, r_ch, mode="entropy"):
        weight_l = len(l_ch) / len(parent)
        weight_r = len(r_ch) / len(parent)
        if mode == "gini":
            gain = self.gini_index(parent) - (weight_l * self.gini_index(l_ch)) + (weight_r * self.gini_index(r_ch))
        else:
            gain = self.entropy(parent) - (weight_l * self.entropy(l_ch)) + (weight_r * self.entropy(r_ch))
        return gain

    def entropy(self, y):
        class_lbls = np.unique(y)
        entropy = 0
        for cls in class_lbls:
            p_cls = len(y[y == cls]) / len(y)
            entropy += -p_cls * np.log2(p_cls)
        return entropy

    def gini_index(self, x):
        total = 0
        for i, xi in enumerate(x[:-1], 1):
            total += np.sum(np.abs(xi - x[i:]))
        if total == 0:
            return total
        else:
            return total / (len(x) ** 2 * np.mean(x))

    def calculate_leaf_val(self, y):
        Y = list(y)
        unique, counts = np.unique(Y, return_counts = True)
        act = dict(zip(unique.astype(int), np.floor(100 * counts / len(Y)).astype(int)))
        if 0 not in act.keys():
            act[0] = 0
        if 1 not in act.keys():
            act[1] = 0
        return act

    def print_tree(self, tree=None, indent = ' ', left_indent = '<<', right_indent='>>'):
        if not tree:
            tree = self.root

        if tree.value is not None:
            tree.printable = f'{indent}{tree.value}'
            print(tree.printable)
        else:
            self.print_tree(tree.left, indent + indent)
            tree.printable = f'{indent}--{features[tree.feature_ind]}<={int(tree.threshold) if tree.threshold.is_integer() else "%.2f" % tree.threshold}'
            print(tree.printable)
            self.print_tree(tree.right, indent + indent)

    def fit(self, X, Y):
        dataset = np.concatenate((X, Y), axis=1)
        self.root = self.build_tree(dataset)

def test(x, tree):
    root = tree.root
    while not root.value:
        if x[root.feature_ind] >= root.threshold and root.right:
            root = root.right
            print('Go right')
        elif x[root.feature_ind] < root.threshold and root.left:
            root = root.left
            print('Go left')

    print('root.value : ', root.value)

if __name__ == '__main__':
    #7 values
    printer_age = np.array([1, 2, 5, 12, 10, 2, 1, 13, 15, 2, 6, 8])

    le = LabelEncoder()
    printer_mark = np.array(le.fit_transform(['NP', 'Canon', 'Samsung', 'Nixon', 'Samsung', 'NP', 'Samsung', 'NP', 'Samsung', 'Nixon', 'NP', 'Samsung']))

    target = np.array([1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0])
    dataset = np.array([printer_age, printer_mark, target])
    dataset = dataset.transpose()
    X, Y = dataset[:, :-1], dataset[:, -1]
    Y = Y.reshape(-1, 1)
    classifier = TreeDecision(min_samples_split=4, max_depth=7)
    classifier.fit(X, Y)

    x_test = np.array([4, 4])
    test(x_test, classifier)
#    classifier.print_tree()