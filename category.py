from sklearn.datasets import load_breast_cancer




def show_labels():
    data = load_breast_cancer()
    label_names = data['target_names']
    labels = data['target']"Lteral['target']" is incompatible with "slicei
    feature_names = data['feature_names']
    features = data['data']
    print(label_names)
    print(labels)


if __name__ == "__main__":
    show_labels()

