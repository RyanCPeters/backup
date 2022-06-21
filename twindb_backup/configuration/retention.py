"""Retention policy configuration"""
from collections import namedtuple

interval_labels = "hourly", "daily", "weekly", "monthly", "yearly"
default_copy_count = 24, 7, 4, 12, 3
RetentionPolicy = namedtuple("RetentionPolicy", interval_labels)

RetentionPolicy._field_defaults.update({k: v for k, v in zip(interval_labels, default_copy_count)})
