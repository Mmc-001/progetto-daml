import tensorflow as tf


# data_augmentation = tf.keras.Sequential([
    # tf.keras.layers.RandomFlip("horizontal"),
    # tf.keras.layers.RandomFlip("vertical"),
    # tf.keras.layers.RandomRotation(0.1),
    # tf.keras.layers.RandomZoom(0.1),
    # tf.keras.layers.RandomContrast(0.1),
# ])

def preprocess(image, label, dataset_info, image_size=(128, 128)):
    image = tf.image.resize(image, image_size)
    image = tf.cast(image, tf.float32) / 255.0
    return image, label

# def preprocess_with_aug(image, label, dataset_info, image_size=(128, 128), data_aug=None):
    # image = tf.image.resize(image, image_size)
    # if data_aug:
        # image = data_aug(image)  # <-- augment here
    # image = tf.cast(image, tf.float32) / 255.0
    # return image, tf.one_hot(label, dataset_info.features['label'].num_classes)
   