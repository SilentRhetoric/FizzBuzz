# flake8: noqa
# fmt: off
# mypy: disable-error-code="no-any-return, no-untyped-call, misc, type-arg"
# This file was automatically generated by algokit-client-generator.
# DO NOT MODIFY IT BY HAND.
# requires: algokit-utils@^1.2.0
import base64
import dataclasses
import decimal
import typing
from abc import ABC, abstractmethod

import algokit_utils
import algosdk
from algosdk.v2client import models
from algosdk.atomic_transaction_composer import (
    AtomicTransactionComposer,
    AtomicTransactionResponse,
    SimulateAtomicTransactionResponse,
    TransactionSigner,
    TransactionWithSigner
)

_APP_SPEC_JSON = r"""{
    "hints": {
        "fizzbuzz()string[]": {
            "call_config": {
                "no_op": "CALL"
            }
        }
    },
    "source": {
        "approval": "I3ByYWdtYSB2ZXJzaW9uIDEwCgpzbWFydF9jb250cmFjdHMuZml6emJ1enouY29udHJhY3QuRml6emJ1enouYXBwcm92YWxfcHJvZ3JhbToKICAgIGludGNibG9jayAyIDEgMCAxMAogICAgYnl0ZWNibG9jayAweDMwMzEzMjMzMzQzNTM2MzczODM5IDB4MDY4MTAxCiAgICBjYWxsc3ViIF9fcHV5YV9hcmM0X3JvdXRlcl9fCiAgICByZXR1cm4KCgovLyBzbWFydF9jb250cmFjdHMuZml6emJ1enouY29udHJhY3QuRml6emJ1enouX19wdXlhX2FyYzRfcm91dGVyX18oKSAtPiB1aW50NjQ6Cl9fcHV5YV9hcmM0X3JvdXRlcl9fOgogICAgLy8gc21hcnRfY29udHJhY3RzL2ZpenpidXp6L2NvbnRyYWN0LnB5OjMKICAgIC8vIGNsYXNzIEZpenpidXp6KEFSQzRDb250cmFjdCk6CiAgICBwcm90byAwIDEKICAgIHR4biBOdW1BcHBBcmdzCiAgICBieiBfX3B1eWFfYXJjNF9yb3V0ZXJfX19iYXJlX3JvdXRpbmdANQogICAgcHVzaGJ5dGVzIDB4ZmNlZjY2MDcgLy8gbWV0aG9kICJmaXp6YnV6eigpc3RyaW5nW10iCiAgICB0eG5hIEFwcGxpY2F0aW9uQXJncyAwCiAgICBtYXRjaCBfX3B1eWFfYXJjNF9yb3V0ZXJfX19maXp6YnV6el9yb3V0ZUAyCiAgICBpbnRjXzIgLy8gMAogICAgcmV0c3ViCgpfX3B1eWFfYXJjNF9yb3V0ZXJfX19maXp6YnV6el9yb3V0ZUAyOgogICAgLy8gc21hcnRfY29udHJhY3RzL2ZpenpidXp6L2NvbnRyYWN0LnB5OjQKICAgIC8vIEBhcmM0LmFiaW1ldGhvZCgpCiAgICB0eG4gT25Db21wbGV0aW9uCiAgICAhCiAgICBhc3NlcnQgLy8gT25Db21wbGV0aW9uIGlzIG5vdCBOb09wCiAgICB0eG4gQXBwbGljYXRpb25JRAogICAgYXNzZXJ0IC8vIGNhbiBvbmx5IGNhbGwgd2hlbiBub3QgY3JlYXRpbmcKICAgIGNhbGxzdWIgZml6emJ1enoKICAgIHB1c2hieXRlcyAweDE1MWY3Yzc1CiAgICBzd2FwCiAgICBjb25jYXQKICAgIGxvZwogICAgaW50Y18xIC8vIDEKICAgIHJldHN1YgoKX19wdXlhX2FyYzRfcm91dGVyX19fYmFyZV9yb3V0aW5nQDU6CiAgICAvLyBzbWFydF9jb250cmFjdHMvZml6emJ1enovY29udHJhY3QucHk6MwogICAgLy8gY2xhc3MgRml6emJ1enooQVJDNENvbnRyYWN0KToKICAgIHR4biBPbkNvbXBsZXRpb24KICAgIGJueiBfX3B1eWFfYXJjNF9yb3V0ZXJfX19hZnRlcl9pZl9lbHNlQDkKICAgIHR4biBBcHBsaWNhdGlvbklECiAgICAhCiAgICBhc3NlcnQgLy8gY2FuIG9ubHkgY2FsbCB3aGVuIGNyZWF0aW5nCiAgICBpbnRjXzEgLy8gMQogICAgcmV0c3ViCgpfX3B1eWFfYXJjNF9yb3V0ZXJfX19hZnRlcl9pZl9lbHNlQDk6CiAgICAvLyBzbWFydF9jb250cmFjdHMvZml6emJ1enovY29udHJhY3QucHk6MwogICAgLy8gY2xhc3MgRml6emJ1enooQVJDNENvbnRyYWN0KToKICAgIGludGNfMiAvLyAwCiAgICByZXRzdWIKCgovLyBzbWFydF9jb250cmFjdHMuZml6emJ1enouY29udHJhY3QuRml6emJ1enouZml6emJ1enooKSAtPiBieXRlczoKZml6emJ1eno6CiAgICAvLyBzbWFydF9jb250cmFjdHMvZml6emJ1enovY29udHJhY3QucHk6NC01CiAgICAvLyBAYXJjNC5hYmltZXRob2QoKQogICAgLy8gZGVmIGZpenpidXp6KHNlbGYpIC0+IGFyYzQuRHluYW1pY0FycmF5W2FyYzQuU3RyaW5nXToKICAgIHByb3RvIDAgMQogICAgLy8gc21hcnRfY29udHJhY3RzL2ZpenpidXp6L2NvbnRyYWN0LnB5OjYKICAgIC8vIHJlc3VsdCA9IGFyYzQuRHluYW1pY0FycmF5W2FyYzQuU3RyaW5nXSgpCiAgICBwdXNoYnl0ZXMgMHgwMDAwCiAgICAvLyBzbWFydF9jb250cmFjdHMvZml6emJ1enovY29udHJhY3QucHk6NwogICAgLy8gZm9yIG4gaW4gdXJhbmdlKDEwMCk6CiAgICBpbnRjXzIgLy8gMAoKZml6emJ1enpfZm9yX2hlYWRlckAxOgogICAgLy8gc21hcnRfY29udHJhY3RzL2ZpenpidXp6L2NvbnRyYWN0LnB5OjcKICAgIC8vIGZvciBuIGluIHVyYW5nZSgxMDApOgogICAgZnJhbWVfZGlnIDEKICAgIHB1c2hpbnQgMTAwIC8vIDEwMAogICAgPAogICAgYnogZml6emJ1enpfYWZ0ZXJfZm9yQDQKICAgIC8vIHNtYXJ0X2NvbnRyYWN0cy9maXp6YnV6ei9jb250cmFjdC5weTo4LTkKICAgIC8vICMgTmVlZCB0byBkbyBPcFVwcyB0byBnZXQgYnVkZ2V0IGZvciB0aGUgbmV4dCBpdGVyYXRpb24gb2YgdGhlIGxvb3AKICAgIC8vIGVuc3VyZV9idWRnZXQoMjU1MCwgT3BVcEZlZVNvdXJjZS5BcHBBY2NvdW50KQogICAgcHVzaGludCAyNTUwIC8vIDI1NTAKICAgIGludGNfMSAvLyAxCiAgICBjYWxsc3ViIGVuc3VyZV9idWRnZXQKICAgIC8vIHNtYXJ0X2NvbnRyYWN0cy9maXp6YnV6ei9jb250cmFjdC5weToxMAogICAgLy8gcmVzdWx0LmFwcGVuZChhcmM0LlN0cmluZyhzZWxmLmRpdmlkZShuICsgMSkpKSAjIFN0YXJ0IGZyb20gMSBub3QgMAogICAgZnJhbWVfZGlnIDEKICAgIGludGNfMSAvLyAxCiAgICArCiAgICBkdXAKICAgIGZyYW1lX2J1cnkgMQogICAgY2FsbHN1YiBkaXZpZGUKICAgIGR1cAogICAgbGVuCiAgICBpdG9iCiAgICBleHRyYWN0IDYgMgogICAgc3dhcAogICAgY29uY2F0CiAgICBmcmFtZV9kaWcgMAogICAgc3dhcAogICAgaW50Y18xIC8vIDEKICAgIGNhbGxzdWIgZHluYW1pY19hcnJheV9jb25jYXRfYnl0ZV9sZW5ndGhfaGVhZAogICAgZnJhbWVfYnVyeSAwCiAgICBiIGZpenpidXp6X2Zvcl9oZWFkZXJAMQoKZml6emJ1enpfYWZ0ZXJfZm9yQDQ6CiAgICAvLyBzbWFydF9jb250cmFjdHMvZml6emJ1enovY29udHJhY3QucHk6MTEKICAgIC8vIHJldHVybiByZXN1bHQKICAgIHJldHN1YgoKCi8vIHNtYXJ0X2NvbnRyYWN0cy5maXp6YnV6ei5jb250cmFjdC5GaXp6YnV6ei5kaXZpZGUobnVtYmVyOiB1aW50NjQpIC0+IGJ5dGVzOgpkaXZpZGU6CiAgICAvLyBzbWFydF9jb250cmFjdHMvZml6emJ1enovY29udHJhY3QucHk6MTMtMTUKICAgIC8vICMgVGhlIGNvcmUgRml6ekJ1enogYWxnb3JpdGhtIGxvZ2ljCiAgICAvLyBAc3Vicm91dGluZQogICAgLy8gZGVmIGRpdmlkZShzZWxmLCBudW1iZXI6IFVJbnQ2NCkgLT4gU3RyaW5nOgogICAgcHJvdG8gMSAxCiAgICAvLyBzbWFydF9jb250cmFjdHMvZml6emJ1enovY29udHJhY3QucHk6MTYKICAgIC8vIGlmIG51bWJlciAlIDMgPT0gMCBhbmQgbnVtYmVyICUgNSA9PSAwOgogICAgZnJhbWVfZGlnIC0xCiAgICBwdXNoaW50IDMgLy8gMwogICAgJQogICAgZHVwCiAgICBibnogZGl2aWRlX2Vsc2VfYm9keUAzCiAgICBmcmFtZV9kaWcgLTEKICAgIHB1c2hpbnQgNSAvLyA1CiAgICAlCiAgICBibnogZGl2aWRlX2Vsc2VfYm9keUAzCiAgICAvLyBzbWFydF9jb250cmFjdHMvZml6emJ1enovY29udHJhY3QucHk6MTcKICAgIC8vIHJldHVybiBTdHJpbmcoIkZpenpCdXp6IikKICAgIHB1c2hieXRlcyAiRml6ekJ1enoiCiAgICBzd2FwCiAgICByZXRzdWIKCmRpdmlkZV9lbHNlX2JvZHlAMzoKICAgIC8vIHNtYXJ0X2NvbnRyYWN0cy9maXp6YnV6ei9jb250cmFjdC5weToxOAogICAgLy8gZWxpZiBudW1iZXIgJSAzID09IDA6CiAgICBmcmFtZV9kaWcgMAogICAgYm56IGRpdmlkZV9lbHNlX2JvZHlANQogICAgLy8gc21hcnRfY29udHJhY3RzL2ZpenpidXp6L2NvbnRyYWN0LnB5OjE5CiAgICAvLyByZXR1cm4gU3RyaW5nKCJGaXp6IikKICAgIHB1c2hieXRlcyAiRml6eiIKICAgIHN3YXAKICAgIHJldHN1YgoKZGl2aWRlX2Vsc2VfYm9keUA1OgogICAgLy8gc21hcnRfY29udHJhY3RzL2ZpenpidXp6L2NvbnRyYWN0LnB5OjIwCiAgICAvLyBlbGlmIG51bWJlciAlIDUgPT0gMDoKICAgIGZyYW1lX2RpZyAtMQogICAgcHVzaGludCA1IC8vIDUKICAgICUKICAgIGJueiBkaXZpZGVfZWxzZV9ib2R5QDcKICAgIC8vIHNtYXJ0X2NvbnRyYWN0cy9maXp6YnV6ei9jb250cmFjdC5weToyMQogICAgLy8gcmV0dXJuIFN0cmluZygiQnV6eiIpCiAgICBwdXNoYnl0ZXMgIkJ1enoiCiAgICBzd2FwCiAgICByZXRzdWIKCmRpdmlkZV9lbHNlX2JvZHlANzoKICAgIC8vIHNtYXJ0X2NvbnRyYWN0cy9maXp6YnV6ei9jb250cmFjdC5weToyMwogICAgLy8gcmV0dXJuIGl0b2EobnVtYmVyKQogICAgZnJhbWVfZGlnIC0xCiAgICBjYWxsc3ViIGl0b2EKICAgIHN3YXAKICAgIHJldHN1YgoKCi8vIHNtYXJ0X2NvbnRyYWN0cy5maXp6YnV6ei5jb250cmFjdC5pdG9hKGludDogdWludDY0KSAtPiBieXRlczoKaXRvYToKICAgIC8vIHNtYXJ0X2NvbnRyYWN0cy9maXp6YnV6ei9jb250cmFjdC5weToyNS0yNwogICAgLy8gIyBVdGlsaXR5IHRvIGNvbnZlcnQgaW50ZWdlcnMtLT5zdHJpbmdzIHNvIHRoZXkgY2FuIGJlIGFkZGVkIHRvIHRoZSByZXN1bHQgYXJyYXkKICAgIC8vIEBzdWJyb3V0aW5lCiAgICAvLyBkZWYgaXRvYShpbnQ6IFVJbnQ2NCkgLT4gU3RyaW5nOgogICAgcHJvdG8gMSAxCiAgICAvLyBzbWFydF9jb250cmFjdHMvZml6emJ1enovY29udHJhY3QucHk6MzAKICAgIC8vIGlmIGludCA8IHJhZGl4OgogICAgZnJhbWVfZGlnIC0xCiAgICAvLyBzbWFydF9jb250cmFjdHMvZml6emJ1enovY29udHJhY3QucHk6MjkKICAgIC8vIHJhZGl4ID0gZGlnaXRzLmxlbmd0aAogICAgaW50Y18zIC8vIDEwCiAgICAvLyBzbWFydF9jb250cmFjdHMvZml6emJ1enovY29udHJhY3QucHk6MzAKICAgIC8vIGlmIGludCA8IHJhZGl4OgogICAgPAogICAgYnogaXRvYV9hZnRlcl9pZl9lbHNlQDIKICAgIC8vIHNtYXJ0X2NvbnRyYWN0cy9maXp6YnV6ei9jb250cmFjdC5weToyOAogICAgLy8gZGlnaXRzID0gQnl0ZXMoYiIwMTIzNDU2Nzg5IikKICAgIGJ5dGVjXzAgLy8gMHgzMDMxMzIzMzM0MzUzNjM3MzgzOQogICAgLy8gc21hcnRfY29udHJhY3RzL2ZpenpidXp6L2NvbnRyYWN0LnB5OjMxCiAgICAvLyByZXR1cm4gU3RyaW5nLmZyb21fYnl0ZXMoZGlnaXRzW2ludF0pCiAgICBmcmFtZV9kaWcgLTEKICAgIGludGNfMSAvLyAxCiAgICBleHRyYWN0MwogICAgcmV0c3ViCgppdG9hX2FmdGVyX2lmX2Vsc2VAMjoKICAgIC8vIHNtYXJ0X2NvbnRyYWN0cy9maXp6YnV6ei9jb250cmFjdC5weTozMgogICAgLy8gcmV0dXJuIGl0b2EoaW50IC8vIHJhZGl4KSArIFN0cmluZy5mcm9tX2J5dGVzKGRpZ2l0c1tpbnQgJSByYWRpeF0pCiAgICBmcmFtZV9kaWcgLTEKICAgIC8vIHNtYXJ0X2NvbnRyYWN0cy9maXp6YnV6ei9jb250cmFjdC5weToyOQogICAgLy8gcmFkaXggPSBkaWdpdHMubGVuZ3RoCiAgICBpbnRjXzMgLy8gMTAKICAgIC8vIHNtYXJ0X2NvbnRyYWN0cy9maXp6YnV6ei9jb250cmFjdC5weTozMgogICAgLy8gcmV0dXJuIGl0b2EoaW50IC8vIHJhZGl4KSArIFN0cmluZy5mcm9tX2J5dGVzKGRpZ2l0c1tpbnQgJSByYWRpeF0pCiAgICAvCiAgICBjYWxsc3ViIGl0b2EKICAgIGZyYW1lX2RpZyAtMQogICAgLy8gc21hcnRfY29udHJhY3RzL2ZpenpidXp6L2NvbnRyYWN0LnB5OjI5CiAgICAvLyByYWRpeCA9IGRpZ2l0cy5sZW5ndGgKICAgIGludGNfMyAvLyAxMAogICAgLy8gc21hcnRfY29udHJhY3RzL2ZpenpidXp6L2NvbnRyYWN0LnB5OjMyCiAgICAvLyByZXR1cm4gaXRvYShpbnQgLy8gcmFkaXgpICsgU3RyaW5nLmZyb21fYnl0ZXMoZGlnaXRzW2ludCAlIHJhZGl4XSkKICAgICUKICAgIC8vIHNtYXJ0X2NvbnRyYWN0cy9maXp6YnV6ei9jb250cmFjdC5weToyOAogICAgLy8gZGlnaXRzID0gQnl0ZXMoYiIwMTIzNDU2Nzg5IikKICAgIGJ5dGVjXzAgLy8gMHgzMDMxMzIzMzM0MzUzNjM3MzgzOQogICAgLy8gc21hcnRfY29udHJhY3RzL2ZpenpidXp6L2NvbnRyYWN0LnB5OjMyCiAgICAvLyByZXR1cm4gaXRvYShpbnQgLy8gcmFkaXgpICsgU3RyaW5nLmZyb21fYnl0ZXMoZGlnaXRzW2ludCAlIHJhZGl4XSkKICAgIHN3YXAKICAgIGludGNfMSAvLyAxCiAgICBleHRyYWN0MwogICAgY29uY2F0CiAgICByZXRzdWIKCgovLyBfcHV5YV9saWIudXRpbC5lbnN1cmVfYnVkZ2V0KHJlcXVpcmVkX2J1ZGdldDogdWludDY0LCBmZWVfc291cmNlOiB1aW50NjQpIC0+IHZvaWQ6CmVuc3VyZV9idWRnZXQ6CiAgICBwcm90byAyIDAKICAgIGZyYW1lX2RpZyAtMgogICAgaW50Y18zIC8vIDEwCiAgICArCgplbnN1cmVfYnVkZ2V0X3doaWxlX3RvcEAxOgogICAgZnJhbWVfZGlnIDAKICAgIGdsb2JhbCBPcGNvZGVCdWRnZXQKICAgID4KICAgIGJ6IGVuc3VyZV9idWRnZXRfYWZ0ZXJfd2hpbGVANwogICAgaXR4bl9iZWdpbgogICAgcHVzaGludCA2IC8vIGFwcGwKICAgIGl0eG5fZmllbGQgVHlwZUVudW0KICAgIHB1c2hpbnQgNSAvLyBEZWxldGVBcHBsaWNhdGlvbgogICAgaXR4bl9maWVsZCBPbkNvbXBsZXRpb24KICAgIGJ5dGVjXzEgLy8gMHgwNjgxMDEKICAgIGl0eG5fZmllbGQgQXBwcm92YWxQcm9ncmFtCiAgICBieXRlY18xIC8vIDB4MDY4MTAxCiAgICBpdHhuX2ZpZWxkIENsZWFyU3RhdGVQcm9ncmFtCiAgICBmcmFtZV9kaWcgLTEKICAgIHN3aXRjaCBlbnN1cmVfYnVkZ2V0X3N3aXRjaF9jYXNlXzBAMyBlbnN1cmVfYnVkZ2V0X3N3aXRjaF9jYXNlXzFANAogICAgYiBlbnN1cmVfYnVkZ2V0X3N3aXRjaF9jYXNlX25leHRANgoKZW5zdXJlX2J1ZGdldF9zd2l0Y2hfY2FzZV8wQDM6CiAgICBpbnRjXzIgLy8gMAogICAgaXR4bl9maWVsZCBGZWUKICAgIGIgZW5zdXJlX2J1ZGdldF9zd2l0Y2hfY2FzZV9uZXh0QDYKCmVuc3VyZV9idWRnZXRfc3dpdGNoX2Nhc2VfMUA0OgogICAgZ2xvYmFsIE1pblR4bkZlZQogICAgaXR4bl9maWVsZCBGZWUKCmVuc3VyZV9idWRnZXRfc3dpdGNoX2Nhc2VfbmV4dEA2OgogICAgaXR4bl9zdWJtaXQKICAgIGIgZW5zdXJlX2J1ZGdldF93aGlsZV90b3BAMQoKZW5zdXJlX2J1ZGdldF9hZnRlcl93aGlsZUA3OgogICAgcmV0c3ViCgoKLy8gX3B1eWFfbGliLmFyYzQuZHluYW1pY19hcnJheV9jb25jYXRfYnl0ZV9sZW5ndGhfaGVhZChhcnJheTogYnl0ZXMsIG5ld19pdGVtc19ieXRlczogYnl0ZXMsIG5ld19pdGVtc19jb3VudDogdWludDY0KSAtPiBieXRlczoKZHluYW1pY19hcnJheV9jb25jYXRfYnl0ZV9sZW5ndGhfaGVhZDoKICAgIHByb3RvIDMgMQogICAgZnJhbWVfZGlnIC0zCiAgICBpbnRjXzIgLy8gMAogICAgZXh0cmFjdF91aW50MTYKICAgIGR1cAogICAgZnJhbWVfZGlnIC0xCiAgICArCiAgICBzd2FwCiAgICBpbnRjXzAgLy8gMgogICAgKgogICAgaW50Y18wIC8vIDIKICAgICsKICAgIGRpZyAxCiAgICBpdG9iCiAgICBleHRyYWN0IDYgMgogICAgZnJhbWVfZGlnIC0zCiAgICBpbnRjXzAgLy8gMgogICAgZGlnIDMKICAgIHN1YnN0cmluZzMKICAgIGZyYW1lX2RpZyAtMQogICAgaW50Y18wIC8vIDIKICAgICoKICAgIGJ6ZXJvCiAgICBjb25jYXQKICAgIGZyYW1lX2RpZyAtMwogICAgbGVuCiAgICBmcmFtZV9kaWcgLTMKICAgIHVuY292ZXIgNAogICAgdW5jb3ZlciAyCiAgICBzdWJzdHJpbmczCiAgICBjb25jYXQKICAgIGZyYW1lX2RpZyAtMgogICAgY29uY2F0CiAgICB1bmNvdmVyIDIKICAgIGludGNfMiAvLyAwCiAgICBjYWxsc3ViIHJlY2FsY3VsYXRlX2hlYWRfZm9yX2VsZW1lbnRzX3dpdGhfYnl0ZV9sZW5ndGhfaGVhZAogICAgY29uY2F0CiAgICByZXRzdWIKCgovLyBfcHV5YV9saWIuYXJjNC5yZWNhbGN1bGF0ZV9oZWFkX2Zvcl9lbGVtZW50c193aXRoX2J5dGVfbGVuZ3RoX2hlYWQoYXJyYXlfaGVhZF9hbmRfdGFpbDogYnl0ZXMsIGxlbmd0aDogdWludDY0LCBzdGFydF9hdF9pbmRleDogdWludDY0KSAtPiBieXRlczoKcmVjYWxjdWxhdGVfaGVhZF9mb3JfZWxlbWVudHNfd2l0aF9ieXRlX2xlbmd0aF9oZWFkOgogICAgcHJvdG8gMyAxCiAgICBmcmFtZV9kaWcgLTIKICAgIGludGNfMCAvLyAyCiAgICAqCiAgICBkdXAKICAgIGZyYW1lX2RpZyAtMQogICAgaW50Y18wIC8vIDIKICAgICoKICAgIGR1cAogICAgY292ZXIgMgogICAgZnJhbWVfZGlnIC0zCiAgICBzd2FwCiAgICBleHRyYWN0X3VpbnQxNgogICAgZnJhbWVfZGlnIC0xCiAgICBzZWxlY3QKCnJlY2FsY3VsYXRlX2hlYWRfZm9yX2VsZW1lbnRzX3dpdGhfYnl0ZV9sZW5ndGhfaGVhZF9mb3JfaGVhZGVyQDE6CiAgICBmcmFtZV9kaWcgMQogICAgZnJhbWVfZGlnIDAKICAgIDwKICAgIGJ6IHJlY2FsY3VsYXRlX2hlYWRfZm9yX2VsZW1lbnRzX3dpdGhfYnl0ZV9sZW5ndGhfaGVhZF9hZnRlcl9mb3JANAogICAgZnJhbWVfZGlnIDIKICAgIGR1cAogICAgaXRvYgogICAgZXh0cmFjdCA2IDIKICAgIGZyYW1lX2RpZyAtMwogICAgZnJhbWVfZGlnIDEKICAgIGR1cAogICAgY292ZXIgNAogICAgdW5jb3ZlciAyCiAgICByZXBsYWNlMwogICAgZHVwCiAgICBmcmFtZV9idXJ5IC0zCiAgICBkaWcgMQogICAgZXh0cmFjdF91aW50MTYKICAgIGludGNfMCAvLyAyCiAgICArCiAgICArCiAgICBmcmFtZV9idXJ5IDIKICAgIGludGNfMCAvLyAyCiAgICArCiAgICBmcmFtZV9idXJ5IDEKICAgIGIgcmVjYWxjdWxhdGVfaGVhZF9mb3JfZWxlbWVudHNfd2l0aF9ieXRlX2xlbmd0aF9oZWFkX2Zvcl9oZWFkZXJAMQoKcmVjYWxjdWxhdGVfaGVhZF9mb3JfZWxlbWVudHNfd2l0aF9ieXRlX2xlbmd0aF9oZWFkX2FmdGVyX2ZvckA0OgogICAgZnJhbWVfZGlnIC0zCiAgICBmcmFtZV9idXJ5IDAKICAgIHJldHN1Ygo=",
        "clear": "I3ByYWdtYSB2ZXJzaW9uIDEwCgpzbWFydF9jb250cmFjdHMuZml6emJ1enouY29udHJhY3QuRml6emJ1enouY2xlYXJfc3RhdGVfcHJvZ3JhbToKICAgIHB1c2hpbnQgMSAvLyAxCiAgICByZXR1cm4K"
    },
    "state": {
        "global": {
            "num_byte_slices": 0,
            "num_uints": 0
        },
        "local": {
            "num_byte_slices": 0,
            "num_uints": 0
        }
    },
    "schema": {
        "global": {
            "declared": {},
            "reserved": {}
        },
        "local": {
            "declared": {},
            "reserved": {}
        }
    },
    "contract": {
        "name": "Fizzbuzz",
        "methods": [
            {
                "name": "fizzbuzz",
                "args": [],
                "returns": {
                    "type": "string[]"
                }
            }
        ],
        "networks": {}
    },
    "bare_call_config": {
        "no_op": "CREATE"
    }
}"""
APP_SPEC = algokit_utils.ApplicationSpecification.from_json(_APP_SPEC_JSON)
_TReturn = typing.TypeVar("_TReturn")


class _ArgsBase(ABC, typing.Generic[_TReturn]):
    @staticmethod
    @abstractmethod
    def method() -> str:
        ...


_TArgs = typing.TypeVar("_TArgs", bound=_ArgsBase[typing.Any])


@dataclasses.dataclass(kw_only=True)
class _TArgsHolder(typing.Generic[_TArgs]):
    args: _TArgs


def _filter_none(value: dict | typing.Any) -> dict | typing.Any:
    if isinstance(value, dict):
        return {k: _filter_none(v) for k, v in value.items() if v is not None}
    return value


def _as_dict(data: typing.Any, *, convert_all: bool = True) -> dict[str, typing.Any]:
    if data is None:
        return {}
    if not dataclasses.is_dataclass(data):
        raise TypeError(f"{data} must be a dataclass")
    if convert_all:
        result = dataclasses.asdict(data) # type: ignore[call-overload]
    else:
        result = {f.name: getattr(data, f.name) for f in dataclasses.fields(data)}
    return _filter_none(result)


def _convert_transaction_parameters(
    transaction_parameters: algokit_utils.TransactionParameters | None,
) -> algokit_utils.TransactionParametersDict:
    return typing.cast(algokit_utils.TransactionParametersDict, _as_dict(transaction_parameters))


def _convert_call_transaction_parameters(
    transaction_parameters: algokit_utils.TransactionParameters | None,
) -> algokit_utils.OnCompleteCallParametersDict:
    return typing.cast(algokit_utils.OnCompleteCallParametersDict, _as_dict(transaction_parameters))


def _convert_create_transaction_parameters(
    transaction_parameters: algokit_utils.TransactionParameters | None,
    on_complete: algokit_utils.OnCompleteActionName,
) -> algokit_utils.CreateCallParametersDict:
    result = typing.cast(algokit_utils.CreateCallParametersDict, _as_dict(transaction_parameters))
    on_complete_enum = on_complete.replace("_", " ").title().replace(" ", "") + "OC"
    result["on_complete"] = getattr(algosdk.transaction.OnComplete, on_complete_enum)
    return result


def _convert_deploy_args(
    deploy_args: algokit_utils.DeployCallArgs | None,
) -> algokit_utils.ABICreateCallArgsDict | None:
    if deploy_args is None:
        return None

    deploy_args_dict = typing.cast(algokit_utils.ABICreateCallArgsDict, _as_dict(deploy_args))
    if isinstance(deploy_args, _TArgsHolder):
        deploy_args_dict["args"] = _as_dict(deploy_args.args)
        deploy_args_dict["method"] = deploy_args.args.method()

    return deploy_args_dict


@dataclasses.dataclass(kw_only=True)
class FizzbuzzArgs(_ArgsBase[list[str]]):
    @staticmethod
    def method() -> str:
        return "fizzbuzz()string[]"


@dataclasses.dataclass(kw_only=True)
class SimulateOptions:
    allow_more_logs: bool = dataclasses.field(default=False)
    allow_empty_signatures: bool = dataclasses.field(default=False)
    extra_opcode_budget: int = dataclasses.field(default=0)
    exec_trace_config: models.SimulateTraceConfig | None         = dataclasses.field(default=None)


class Composer:

    def __init__(self, app_client: algokit_utils.ApplicationClient, atc: AtomicTransactionComposer):
        self.app_client = app_client
        self.atc = atc

    def build(self) -> AtomicTransactionComposer:
        return self.atc

    def simulate(self, options: SimulateOptions | None = None) -> SimulateAtomicTransactionResponse:
        request = models.SimulateRequest(
            allow_more_logs=options.allow_more_logs,
            allow_empty_signatures=options.allow_empty_signatures,
            extra_opcode_budget=options.extra_opcode_budget,
            exec_trace_config=options.exec_trace_config,
            txn_groups=[]
        ) if options else None
        result = self.atc.simulate(self.app_client.algod_client, request)
        return result

    def execute(self) -> AtomicTransactionResponse:
        return self.app_client.execute_atc(self.atc)

    def fizzbuzz(
        self,
        *,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> "Composer":
        """Adds a call to `fizzbuzz()string[]` ABI method
        
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns Composer: This Composer instance"""

        args = FizzbuzzArgs()
        self.app_client.compose_call(
            self.atc,
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return self

    def create_bare(
        self,
        *,
        on_complete: typing.Literal["no_op"] = "no_op",
        transaction_parameters: algokit_utils.CreateTransactionParameters | None = None,
    ) -> "Composer":
        """Adds a call to create an application using the no_op bare method
        
        :param typing.Literal[no_op] on_complete: On completion type to use
        :param algokit_utils.CreateTransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns Composer: This Composer instance"""

        self.app_client.compose_create(
            self.atc,
            call_abi_method=False,
            transaction_parameters=_convert_create_transaction_parameters(transaction_parameters, on_complete),
        )
        return self

    def clear_state(
        self,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
        app_args: list[bytes] | None = None,
    ) -> "Composer":
        """Adds a call to the application with on completion set to ClearState
    
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :param list[bytes] | None app_args: (optional) Application args to pass"""
    
        self.app_client.compose_clear_state(self.atc, _convert_transaction_parameters(transaction_parameters), app_args)
        return self


class FizzbuzzClient:
    """A class for interacting with the Fizzbuzz app providing high productivity and
    strongly typed methods to deploy and call the app"""

    @typing.overload
    def __init__(
        self,
        algod_client: algosdk.v2client.algod.AlgodClient,
        *,
        app_id: int = 0,
        signer: TransactionSigner | algokit_utils.Account | None = None,
        sender: str | None = None,
        suggested_params: algosdk.transaction.SuggestedParams | None = None,
        template_values: algokit_utils.TemplateValueMapping | None = None,
        app_name: str | None = None,
    ) -> None:
        ...

    @typing.overload
    def __init__(
        self,
        algod_client: algosdk.v2client.algod.AlgodClient,
        *,
        creator: str | algokit_utils.Account,
        indexer_client: algosdk.v2client.indexer.IndexerClient | None = None,
        existing_deployments: algokit_utils.AppLookup | None = None,
        signer: TransactionSigner | algokit_utils.Account | None = None,
        sender: str | None = None,
        suggested_params: algosdk.transaction.SuggestedParams | None = None,
        template_values: algokit_utils.TemplateValueMapping | None = None,
        app_name: str | None = None,
    ) -> None:
        ...

    def __init__(
        self,
        algod_client: algosdk.v2client.algod.AlgodClient,
        *,
        creator: str | algokit_utils.Account | None = None,
        indexer_client: algosdk.v2client.indexer.IndexerClient | None = None,
        existing_deployments: algokit_utils.AppLookup | None = None,
        app_id: int = 0,
        signer: TransactionSigner | algokit_utils.Account | None = None,
        sender: str | None = None,
        suggested_params: algosdk.transaction.SuggestedParams | None = None,
        template_values: algokit_utils.TemplateValueMapping | None = None,
        app_name: str | None = None,
    ) -> None:
        """
        FizzbuzzClient can be created with an app_id to interact with an existing application, alternatively
        it can be created with a creator and indexer_client specified to find existing applications by name and creator.
        
        :param AlgodClient algod_client: AlgoSDK algod client
        :param int app_id: The app_id of an existing application, to instead find the application by creator and name
        use the creator and indexer_client parameters
        :param str | Account creator: The address or Account of the app creator to resolve the app_id
        :param IndexerClient indexer_client: AlgoSDK indexer client, only required if deploying or finding app_id by
        creator and app name
        :param AppLookup existing_deployments:
        :param TransactionSigner | Account signer: Account or signer to use to sign transactions, if not specified and
        creator was passed as an Account will use that.
        :param str sender: Address to use as the sender for all transactions, will use the address associated with the
        signer if not specified.
        :param TemplateValueMapping template_values: Values to use for TMPL_* template variables, dictionary keys should
        *NOT* include the TMPL_ prefix
        :param str | None app_name: Name of application to use when deploying, defaults to name defined on the
        Application Specification
            """

        self.app_spec = APP_SPEC
        
        # calling full __init__ signature, so ignoring mypy warning about overloads
        self.app_client = algokit_utils.ApplicationClient(  # type: ignore[call-overload, misc]
            algod_client=algod_client,
            app_spec=self.app_spec,
            app_id=app_id,
            creator=creator,
            indexer_client=indexer_client,
            existing_deployments=existing_deployments,
            signer=signer,
            sender=sender,
            suggested_params=suggested_params,
            template_values=template_values,
            app_name=app_name,
        )

    @property
    def algod_client(self) -> algosdk.v2client.algod.AlgodClient:
        return self.app_client.algod_client

    @property
    def app_id(self) -> int:
        return self.app_client.app_id

    @app_id.setter
    def app_id(self, value: int) -> None:
        self.app_client.app_id = value

    @property
    def app_address(self) -> str:
        return self.app_client.app_address

    @property
    def sender(self) -> str | None:
        return self.app_client.sender

    @sender.setter
    def sender(self, value: str) -> None:
        self.app_client.sender = value

    @property
    def signer(self) -> TransactionSigner | None:
        return self.app_client.signer

    @signer.setter
    def signer(self, value: TransactionSigner) -> None:
        self.app_client.signer = value

    @property
    def suggested_params(self) -> algosdk.transaction.SuggestedParams | None:
        return self.app_client.suggested_params

    @suggested_params.setter
    def suggested_params(self, value: algosdk.transaction.SuggestedParams | None) -> None:
        self.app_client.suggested_params = value

    def fizzbuzz(
        self,
        *,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> algokit_utils.ABITransactionResponse[list[str]]:
        """Calls `fizzbuzz()string[]` ABI method
        
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns algokit_utils.ABITransactionResponse[list[str]]: The result of the transaction"""

        args = FizzbuzzArgs()
        result = self.app_client.call(
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return result

    def create_bare(
        self,
        *,
        on_complete: typing.Literal["no_op"] = "no_op",
        transaction_parameters: algokit_utils.CreateTransactionParameters | None = None,
    ) -> algokit_utils.TransactionResponse:
        """Creates an application using the no_op bare method
        
        :param typing.Literal[no_op] on_complete: On completion type to use
        :param algokit_utils.CreateTransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns algokit_utils.TransactionResponse: The result of the transaction"""

        result = self.app_client.create(
            call_abi_method=False,
            transaction_parameters=_convert_create_transaction_parameters(transaction_parameters, on_complete),
        )
        return result

    def clear_state(
        self,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
        app_args: list[bytes] | None = None,
    ) -> algokit_utils.TransactionResponse:
        """Calls the application with on completion set to ClearState
    
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :param list[bytes] | None app_args: (optional) Application args to pass
        :returns algokit_utils.TransactionResponse: The result of the transaction"""
    
        return self.app_client.clear_state(_convert_transaction_parameters(transaction_parameters), app_args)

    def deploy(
        self,
        version: str | None = None,
        *,
        signer: TransactionSigner | None = None,
        sender: str | None = None,
        allow_update: bool | None = None,
        allow_delete: bool | None = None,
        on_update: algokit_utils.OnUpdate = algokit_utils.OnUpdate.Fail,
        on_schema_break: algokit_utils.OnSchemaBreak = algokit_utils.OnSchemaBreak.Fail,
        template_values: algokit_utils.TemplateValueMapping | None = None,
        create_args: algokit_utils.DeployCallArgs | None = None,
        update_args: algokit_utils.DeployCallArgs | None = None,
        delete_args: algokit_utils.DeployCallArgs | None = None,
    ) -> algokit_utils.DeployResponse:
        """Deploy an application and update client to reference it.
        
        Idempotently deploy (create, update/delete if changed) an app against the given name via the given creator
        account, including deploy-time template placeholder substitutions.
        To understand the architecture decisions behind this functionality please see
        <https://github.com/algorandfoundation/algokit-cli/blob/main/docs/architecture-decisions/2023-01-12_smart-contract-deployment.md>
        
        ```{note}
        If there is a breaking state schema change to an existing app (and `on_schema_break` is set to
        'ReplaceApp' the existing app will be deleted and re-created.
        ```
        
        ```{note}
        If there is an update (different TEAL code) to an existing app (and `on_update` is set to 'ReplaceApp')
        the existing app will be deleted and re-created.
        ```
        
        :param str version: version to use when creating or updating app, if None version will be auto incremented
        :param algosdk.atomic_transaction_composer.TransactionSigner signer: signer to use when deploying app
        , if None uses self.signer
        :param str sender: sender address to use when deploying app, if None uses self.sender
        :param bool allow_delete: Used to set the `TMPL_DELETABLE` template variable to conditionally control if an app
        can be deleted
        :param bool allow_update: Used to set the `TMPL_UPDATABLE` template variable to conditionally control if an app
        can be updated
        :param OnUpdate on_update: Determines what action to take if an application update is required
        :param OnSchemaBreak on_schema_break: Determines what action to take if an application schema requirements
        has increased beyond the current allocation
        :param dict[str, int|str|bytes] template_values: Values to use for `TMPL_*` template variables, dictionary keys
        should *NOT* include the TMPL_ prefix
        :param algokit_utils.DeployCallArgs | None create_args: Arguments used when creating an application
        :param algokit_utils.DeployCallArgs | None update_args: Arguments used when updating an application
        :param algokit_utils.DeployCallArgs | None delete_args: Arguments used when deleting an application
        :return DeployResponse: details action taken and relevant transactions
        :raises DeploymentError: If the deployment failed"""

        return self.app_client.deploy(
            version,
            signer=signer,
            sender=sender,
            allow_update=allow_update,
            allow_delete=allow_delete,
            on_update=on_update,
            on_schema_break=on_schema_break,
            template_values=template_values,
            create_args=_convert_deploy_args(create_args),
            update_args=_convert_deploy_args(update_args),
            delete_args=_convert_deploy_args(delete_args),
        )

    def compose(self, atc: AtomicTransactionComposer | None = None) -> Composer:
        return Composer(self.app_client, atc or AtomicTransactionComposer())