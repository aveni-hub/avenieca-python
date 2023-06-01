from dataclasses import dataclass
from typing import Optional

from avenieca.data import Base


@dataclass
class HNSW(Base):
    # Minimal size (in KiloBytes) of vectors for additional payload-based indexing.
    # If payload chunk is smaller than `full_scan_threshold` additional indexing won't be used -
    # in this case full-scan search should be preferred by query planner and additional indexing is not required.
    # Note: 1Kb = 1 vector of size 256
    full_scan_threshold: Optional[int] = 10000
    # Number of parallel threads used for background index building. If 0 - auto selection.
    max_indexing_threads: Optional[int] = 0
    # Number of edges per node in the index graph. Larger the value - more accurate the search, more space required.
    m: Optional[int] = 16
    # Number of neighbours to consider during the index building. Larger the value - more accurate the search,
    # more time required to build index.
    ef_construct: Optional[int] = 100


@dataclass
class WAL(Base):
    # Size of a single WAL block file
    wal_capacity_mb: Optional[int] = 32
    # Number of segments to create in advance
    wal_segments_ahead: Optional[int] = 0


@dataclass
class Optimizer(Base):
    # The minimal fraction of deleted vectors in a segment, required to perform segment optimization
    deleted_threshold: Optional[float] = 0.2
    # The minimal number of vectors in a segment, required to perform segment optimization
    vacuum_min_vector_number: Optional[int] = 1000
    # Target amount of segments optimizer will try to keep.
    # Real amount of segments may vary depending on multiple parameters:
    #
    # - Amount of stored points.
    # - Current write RPS.
    #
    # It is recommended to select default number of segments as a factor of the number of search threads,
    # so that each segment would be handled evenly by one of the threads.
    default_segment_number: Optional[int] = 0
    # Do not create segments larger this size (in KiloBytes).
    # Large segments might require disproportionately long indexation times,
    # therefore it makes sense to limit the size of segments.
    #
    # If indexation speed have more priority for your - make this parameter lower.
    # If search speed is more important - make this parameter higher.
    # Note: 1Kb = 1 vector of size 256
    max_segment_size: Optional[int] = None
    #
    # Maximum size (in KiloBytes) of vectors to store in-memory per segment.
    # Segments larger than this threshold will be stored as read-only memmaped file.
    # To enable memmap storage, lower the threshold
    # Note: 1Kb = 1 vector of size 256
    memmap_threshold: Optional[int] = None
    # Maximum size (in KiloBytes) of vectors allowed for plain index.
    # Default value based on <https://github.com/google-research/google-research/blob/master/scann/docs/algorithms.md>
    # Note: 1Kb = 1 vector of size 256
    indexing_threshold: Optional[int] = 2000
    # Interval between forced flushes.
    flush_interval_sec: Optional[int] = 5
    # Max number of threads, which can be used for optimization. If 0 - `NUM_CPU - 1` will be used
    max_optimization_threads: Optional[int] = 1


@dataclass
class VSE(Base):
    hnsw_config: HNSW
    wal_config: WAL
    optimizer_config: Optimizer
    shard_number: Optional[int]
    # Wait timeout for operation commit in seconds, if not specified - default value will be supplied
    timeout: Optional[int] = 10
    vse_url: str = "http://localhost:6334"
    similarity_metric: str = "euclid"
    # If true - point's payload will not be stored in memory
    on_disk_payload: Optional[bool] = None
