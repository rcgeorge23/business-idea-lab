# Test fixtures

`raw_items.jsonl` contains **synthetic** items written for unit tests only. The
authors, URLs, repositories and statements are invented to exercise the
extractor, deduplicator, clusterer, ranker and observation renderer. They are
**not** evidence, must never be cited in a discovery run, and are not part of the
PoC evidence base. URLs point at plausible-looking but non-existent or
illustrative locations.

Designed properties:

- a recurring accounting/manual-rekey pattern across several independent authors;
- a recurring e-commerce order re-keying pattern;
- one repost that must be detected as a duplicate and never counted twice;
- one vendor-marketing item, one empty item and one cue-free item that must be
  rejected by extraction with specific reasons;
- one change-cue item (MTD/HMRC) to exercise the change-driven archetype;
- one transient incident for the transient penalty path.
