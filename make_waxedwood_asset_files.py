#!/usr/bin/env python3
import sys, os
from os import path

VANILLA_WOOD = [
        "oak",
        "spruce",
        "birch",
        "jungle",
        "acacia",
        "dark_oak",
        # not including crimson and warped -- they're already fireproof
        ]

MOD_WOOD = {
        #TODO
        }

assert path.exists(path.join(os.getcwd(), "make_waxedwood_asset_files.py")), "Not in correct directory"

resources_dir = path.join(os.getcwd(), "src", "main", "resources")
block_models_dir = path.join(resources_dir, "assets", "waxedwood", "models", "block")
item_models_dir = path.join(resources_dir, "assets", "waxedwood", "models", "item")
block_states_dir = path.join(resources_dir, "assets", "waxedwood", "blockstates")
lang_file = path.join(resources_dir, "assets", "waxedwood", "lang", "en_us.json")
block_loot_tables_dir = path.join(resources_dir, "data", "waxedwood", "loot_tables", "blocks")
tags_dir = path.join(resources_dir, "data", "minecraft", "tags", "blocks")
    # "minecraft" instead of "waxedwood", so we add to vanilla's tags eg minecraft:planks

def item_model_for(name):
    return """{
  "parent": "minecraft:block/""" + name + """\"
}"""

def loot_table_for(name):
    return """{
  "type": "minecraft:block",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "waxedwood:waxed_""" + name + """\"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:survives_explosion"
        }
      ]
    }
  ]
}"""

def block_states_for_planks(wood):
    return """{
  "variants": {
    "": {
      "model": "minecraft:block/""" + wood + """_planks"
    }
  }
}"""

def block_states_for_stairs(wood):
    return """{
  "variants": {
    "facing=east,half=bottom,shape=inner_left": {
      "model": "minecraft:block/""" + wood + """_stairs_inner",
      "y": 270,
      "uvlock": true
    },
    "facing=east,half=bottom,shape=inner_right": {
      "model": "minecraft:block/""" + wood + """_stairs_inner"
    },
    "facing=east,half=bottom,shape=outer_left": {
      "model": "minecraft:block/""" + wood + """_stairs_outer",
      "y": 270,
      "uvlock": true
    },
    "facing=east,half=bottom,shape=outer_right": {
      "model": "minecraft:block/""" + wood + """_stairs_outer"
    },
    "facing=east,half=bottom,shape=straight": {
      "model": "minecraft:block/""" + wood + """_stairs"
    },
    "facing=east,half=top,shape=inner_left": {
      "model": "minecraft:block/""" + wood + """_stairs_inner",
      "x": 180,
      "uvlock": true
    },
    "facing=east,half=top,shape=inner_right": {
      "model": "minecraft:block/""" + wood + """_stairs_inner",
      "x": 180,
      "y": 90,
      "uvlock": true
    },
    "facing=east,half=top,shape=outer_left": {
      "model": "minecraft:block/""" + wood + """_stairs_outer",
      "x": 180,
      "uvlock": true
    },
    "facing=east,half=top,shape=outer_right": {
      "model": "minecraft:block/""" + wood + """_stairs_outer",
      "x": 180,
      "y": 90,
      "uvlock": true
    },
    "facing=east,half=top,shape=straight": {
      "model": "minecraft:block/""" + wood + """_stairs",
      "x": 180,
      "uvlock": true
    },
    "facing=north,half=bottom,shape=inner_left": {
      "model": "minecraft:block/""" + wood + """_stairs_inner",
      "y": 180,
      "uvlock": true
    },
    "facing=north,half=bottom,shape=inner_right": {
      "model": "minecraft:block/""" + wood + """_stairs_inner",
      "y": 270,
      "uvlock": true
    },
    "facing=north,half=bottom,shape=outer_left": {
      "model": "minecraft:block/""" + wood + """_stairs_outer",
      "y": 180,
      "uvlock": true
    },
    "facing=north,half=bottom,shape=outer_right": {
      "model": "minecraft:block/""" + wood + """_stairs_outer",
      "y": 270,
      "uvlock": true
    },
    "facing=north,half=bottom,shape=straight": {
      "model": "minecraft:block/""" + wood + """_stairs",
      "y": 270,
      "uvlock": true
    },
    "facing=north,half=top,shape=inner_left": {
      "model": "minecraft:block/""" + wood + """_stairs_inner",
      "x": 180,
      "y": 270,
      "uvlock": true
    },
    "facing=north,half=top,shape=inner_right": {
      "model": "minecraft:block/""" + wood + """_stairs_inner",
      "x": 180,
      "uvlock": true
    },
    "facing=north,half=top,shape=outer_left": {
      "model": "minecraft:block/""" + wood + """_stairs_outer",
      "x": 180,
      "y": 270,
      "uvlock": true
    },
    "facing=north,half=top,shape=outer_right": {
      "model": "minecraft:block/""" + wood + """_stairs_outer",
      "x": 180,
      "uvlock": true
    },
    "facing=north,half=top,shape=straight": {
      "model": "minecraft:block/""" + wood + """_stairs",
      "x": 180,
      "y": 270,
      "uvlock": true
    },
    "facing=south,half=bottom,shape=inner_left": {
      "model": "minecraft:block/""" + wood + """_stairs_inner"
    },
    "facing=south,half=bottom,shape=inner_right": {
      "model": "minecraft:block/""" + wood + """_stairs_inner",
      "y": 90,
      "uvlock": true
    },
    "facing=south,half=bottom,shape=outer_left": {
      "model": "minecraft:block/""" + wood + """_stairs_outer"
    },
    "facing=south,half=bottom,shape=outer_right": {
      "model": "minecraft:block/""" + wood + """_stairs_outer",
      "y": 90,
      "uvlock": true
    },
    "facing=south,half=bottom,shape=straight": {
      "model": "minecraft:block/""" + wood + """_stairs",
      "y": 90,
      "uvlock": true
    },
    "facing=south,half=top,shape=inner_left": {
      "model": "minecraft:block/""" + wood + """_stairs_inner",
      "x": 180,
      "y": 90,
      "uvlock": true
    },
    "facing=south,half=top,shape=inner_right": {
      "model": "minecraft:block/""" + wood + """_stairs_inner",
      "x": 180,
      "y": 180,
      "uvlock": true
    },
    "facing=south,half=top,shape=outer_left": {
      "model": "minecraft:block/""" + wood + """_stairs_outer",
      "x": 180,
      "y": 90,
      "uvlock": true
    },
    "facing=south,half=top,shape=outer_right": {
      "model": "minecraft:block/""" + wood + """_stairs_outer",
      "x": 180,
      "y": 180,
      "uvlock": true
    },
    "facing=south,half=top,shape=straight": {
      "model": "minecraft:block/""" + wood + """_stairs",
      "x": 180,
      "y": 90,
      "uvlock": true
    },
    "facing=west,half=bottom,shape=inner_left": {
      "model": "minecraft:block/""" + wood + """_stairs_inner",
      "y": 90,
      "uvlock": true
    },
    "facing=west,half=bottom,shape=inner_right": {
      "model": "minecraft:block/""" + wood + """_stairs_inner",
      "y": 180,
      "uvlock": true
    },
    "facing=west,half=bottom,shape=outer_left": {
      "model": "minecraft:block/""" + wood + """_stairs_outer",
      "y": 90,
      "uvlock": true
    },
    "facing=west,half=bottom,shape=outer_right": {
      "model": "minecraft:block/""" + wood + """_stairs_outer",
      "y": 180,
      "uvlock": true
    },
    "facing=west,half=bottom,shape=straight": {
      "model": "minecraft:block/""" + wood + """_stairs",
      "y": 180,
      "uvlock": true
    },
    "facing=west,half=top,shape=inner_left": {
      "model": "minecraft:block/""" + wood + """_stairs_inner",
      "x": 180,
      "y": 180,
      "uvlock": true
    },
    "facing=west,half=top,shape=inner_right": {
      "model": "minecraft:block/""" + wood + """_stairs_inner",
      "x": 180,
      "y": 270,
      "uvlock": true
    },
    "facing=west,half=top,shape=outer_left": {
      "model": "minecraft:block/""" + wood + """_stairs_outer",
      "x": 180,
      "y": 180,
      "uvlock": true
    },
    "facing=west,half=top,shape=outer_right": {
      "model": "minecraft:block/""" + wood + """_stairs_outer",
      "x": 180,
      "y": 270,
      "uvlock": true
    },
    "facing=west,half=top,shape=straight": {
      "model": "minecraft:block/""" + wood + """_stairs",
      "x": 180,
      "y": 180,
      "uvlock": true
    }
  }
}"""

def block_states_for_slab(wood):
    return """{
  "variants": {
    "type=bottom": {
      "model": "minecraft:block/""" + wood + """_slab"
    },
    "type=double": {
      "model": "minecraft:block/""" + wood + """_planks"
    },
    "type=top": {
      "model": "minecraft:block/""" + wood + """_slab_top"
    }
  }
}"""

def block_states_for_gate(wood):
    return """{
  "variants": {
    "facing=east,in_wall=false,open=false": {
      "uvlock": true,
      "y": 270,
      "model": "minecraft:block/""" + wood + """_fence_gate"
    },
    "facing=east,in_wall=false,open=true": {
      "uvlock": true,
      "y": 270,
      "model": "minecraft:block/""" + wood + """_fence_gate_open"
    },
    "facing=east,in_wall=true,open=false": {
      "uvlock": true,
      "y": 270,
      "model": "minecraft:block/""" + wood + """_fence_gate_wall"
    },
    "facing=east,in_wall=true,open=true": {
      "uvlock": true,
      "y": 270,
      "model": "minecraft:block/""" + wood + """_fence_gate_wall_open"
    },
    "facing=north,in_wall=false,open=false": {
      "uvlock": true,
      "y": 180,
      "model": "minecraft:block/""" + wood + """_fence_gate"
    },
    "facing=north,in_wall=false,open=true": {
      "uvlock": true,
      "y": 180,
      "model": "minecraft:block/""" + wood + """_fence_gate_open"
    },
    "facing=north,in_wall=true,open=false": {
      "uvlock": true,
      "y": 180,
      "model": "minecraft:block/""" + wood + """_fence_gate_wall"
    },
    "facing=north,in_wall=true,open=true": {
      "uvlock": true,
      "y": 180,
      "model": "minecraft:block/""" + wood + """_fence_gate_wall_open"
    },
    "facing=south,in_wall=false,open=false": {
      "uvlock": true,
      "model": "minecraft:block/""" + wood + """_fence_gate"
    },
    "facing=south,in_wall=false,open=true": {
      "uvlock": true,
      "model": "minecraft:block/""" + wood + """_fence_gate_open"
    },
    "facing=south,in_wall=true,open=false": {
      "uvlock": true,
      "model": "minecraft:block/""" + wood + """_fence_gate_wall"
    },
    "facing=south,in_wall=true,open=true": {
      "uvlock": true,
      "model": "minecraft:block/""" + wood + """_fence_gate_wall_open"
    },
    "facing=west,in_wall=false,open=false": {
      "uvlock": true,
      "y": 90,
      "model": "minecraft:block/""" + wood + """_fence_gate"
    },
    "facing=west,in_wall=false,open=true": {
      "uvlock": true,
      "y": 90,
      "model": "minecraft:block/""" + wood + """_fence_gate_open"
    },
    "facing=west,in_wall=true,open=false": {
      "uvlock": true,
      "y": 90,
      "model": "minecraft:block/""" + wood + """_fence_gate_wall"
    },
    "facing=west,in_wall=true,open=true": {
      "uvlock": true,
      "y": 90,
      "model": "minecraft:block/""" + wood + """_fence_gate_wall_open"
    }
  }
}"""

def block_states_for_fence(wood):
    return """{
  "multipart": [
    {
      "apply": {
        "model": "minecraft:block/""" + wood + """_fence_post"
      }
    },
    {
      "when": {
        "north": "true"
      },
      "apply": {
        "model": "minecraft:block/""" + wood + """_fence_side",
        "uvlock": true
      }
    },
    {
      "when": {
        "east": "true"
      },
      "apply": {
        "model": "minecraft:block/""" + wood + """_fence_side",
        "y": 90,
        "uvlock": true
      }
    },
    {
      "when": {
        "south": "true"
      },
      "apply": {
        "model": "minecraft:block/""" + wood + """_fence_side",
        "y": 180,
        "uvlock": true
      }
    },
    {
      "when": {
        "west": "true"
      },
      "apply": {
        "model": "minecraft:block/""" + wood + """_fence_side",
        "y": 270,
        "uvlock": true
      }
    }
  ]
}"""

def block_states_for_log(wood):
    return """{
  "variants": {
    "axis=x": {
      "model": "minecraft:block/""" + wood + """_log_horizontal",
      "x": 90,
      "y": 90
    },
    "axis=y": {
      "model": "minecraft:block/""" + wood + """_log"
    },
    "axis=z": {
      "model": "minecraft:block/""" + wood + """_log_horizontal",
      "x": 90
    }
  }
}"""

def block_states_for_stripped_log(wood):
    return """{
  "variants": {
    "axis=x": {
      "model": "minecraft:block/stripped_""" + wood + """_log_horizontal",
      "x": 90,
      "y": 90
    },
    "axis=y": {
      "model": "minecraft:block/stripped_""" + wood + """_log"
    },
    "axis=z": {
      "model": "minecraft:block/stripped_""" + wood + """_log_horizontal",
      "x": 90
    }
  }
}"""

def block_states_for_wood(wood):
    return """{
  "variants": {
    "axis=x": {
      "model": "minecraft:block/""" + wood + """_wood",
      "x": 90,
      "y": 90
    },
    "axis=y": {
      "model": "minecraft:block/""" + wood + """_wood"
    },
    "axis=z": {
      "model": "minecraft:block/""" + wood + """_wood",
      "x": 90
    }
  }
}"""

def block_states_for_stripped_wood(wood):
    return """{
  "variants": {
    "axis=x": {
      "model": "minecraft:block/stripped_""" + wood + """_wood",
      "x": 90,
      "y": 90
    },
    "axis=y": {
      "model": "minecraft:block/stripped_""" + wood + """_wood"
    },
    "axis=z": {
      "model": "minecraft:block/stripped_""" + wood + """_wood",
      "x": 90
    }
  }
}"""


def write_planks_resources(wood):
    with open(path.join(item_models_dir, "waxed_" + wood + "_planks.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(wood + "_planks"))
    with open(path.join(block_loot_tables_dir, "waxed_" + wood + "_planks.json"), "w") as loot:
        loot.write(loot_table_for(wood + "_planks"))
    with open(path.join(block_states_dir, "waxed_" + wood + "_planks.json"), "w") as blockstates:
        blockstates.write(block_states_for_planks(wood))

def write_stairs_resources(wood):
    with open(path.join(item_models_dir, "waxed_" + wood + "_stairs.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(wood + "_stairs"))
    with open(path.join(block_loot_tables_dir, "waxed_" + wood + "_stairs.json"), "w") as loot:
        loot.write(loot_table_for(wood + "_stairs"))
    with open(path.join(block_states_dir, "waxed_" + wood + "_stairs.json"), "w") as blockstates:
        blockstates.write(block_states_for_stairs(wood))

def write_slab_resources(wood):
    with open(path.join(item_models_dir, "waxed_" + wood + "_slab.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(wood + "_slab"))
    with open(path.join(block_loot_tables_dir, "waxed_" + wood + "_slab.json"), "w") as loot:
        loot.write(loot_table_for(wood + "_slab"))
    with open(path.join(block_states_dir, "waxed_" + wood + "_slab.json"), "w") as blockstates:
        blockstates.write(block_states_for_slab(wood))

def write_gate_resources(wood):
    with open(path.join(item_models_dir, "waxed_" + wood + "_fence_gate.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(wood + "_fence_gate"))
    with open(path.join(block_loot_tables_dir, "waxed_" + wood + "_fence_gate.json"), "w") as loot:
        loot.write(loot_table_for(wood + "_fence_gate"))
    with open(path.join(block_states_dir, "waxed_" + wood + "_fence_gate.json"), "w") as blockstates:
        blockstates.write(block_states_for_gate(wood))

def write_fence_resources(wood):
    with open(path.join(item_models_dir, "waxed_" + wood + "_fence.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(wood + "_fence_inventory")) # Note using a different model for item
    with open(path.join(block_loot_tables_dir, "waxed_" + wood + "_fence.json"), "w") as loot:
        loot.write(loot_table_for(wood + "_fence"))
    with open(path.join(block_states_dir, "waxed_" + wood + "_fence.json"), "w") as blockstates:
        blockstates.write(block_states_for_fence(wood))

def write_log_resources(wood):
    with open(path.join(item_models_dir, "waxed_" + wood + "_log.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(wood + "_log"))
    with open(path.join(block_loot_tables_dir, "waxed_" + wood + "_log.json"), "w") as loot:
        loot.write(loot_table_for(wood + "_log"))
    with open(path.join(block_states_dir, "waxed_" + wood + "_log.json"), "w") as blockstates:
        blockstates.write(block_states_for_log(wood))

def write_stripped_log_resources(wood):
    with open(path.join(item_models_dir, "waxed_stripped_" + wood + "_log.json"), "w") as itemmodel:
        itemmodel.write(item_model_for("stripped_" + wood + "_log"))
    with open(path.join(block_loot_tables_dir, "waxed_stripped_" + wood + "_log.json"), "w") as loot:
        loot.write(loot_table_for(wood + "_stripped_log"))
    with open(path.join(block_states_dir, "waxed_stripped_" + wood + "_log.json"), "w") as blockstates:
        blockstates.write(block_states_for_stripped_log(wood))

def write_wood_resources(wood):
    with open(path.join(item_models_dir, "waxed_" + wood + "_wood.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(wood + "_wood"))
    with open(path.join(block_loot_tables_dir, "waxed_" + wood + "_wood.json"), "w") as loot:
        loot.write(loot_table_for(wood + "_wood"))
    with open(path.join(block_states_dir, "waxed_" + wood + "_wood.json"), "w") as blockstates:
        blockstates.write(block_states_for_wood(wood))

def write_stripped_wood_resources(wood):
    with open(path.join(item_models_dir, "waxed_stripped_" + wood + "_wood.json"), "w") as itemmodel:
        itemmodel.write(item_model_for("stripped_" + wood + "_wood"))
    with open(path.join(block_loot_tables_dir, "waxed_stripped_" + wood + "_wood.json"), "w") as loot:
        loot.write(loot_table_for(wood + "_stripped_wood"))
    with open(path.join(block_states_dir, "waxed_stripped_" + wood + "_wood.json"), "w") as blockstates:
        blockstates.write(block_states_for_stripped_wood(wood))

for wood in VANILLA_WOOD:
    write_planks_resources(wood)
    write_stairs_resources(wood)
    write_slab_resources(wood)
    write_gate_resources(wood)
    write_fence_resources(wood)
    write_log_resources(wood)
    write_stripped_log_resources(wood)
    write_wood_resources(wood)
    write_stripped_wood_resources(wood)
    # Note: Don't need to do trapdoors, doors, and signs, since they're already fireproof in vanilla.
    # TODO recipes!

with open(lang_file, "w") as lang:
    lang.write("{\n")
    for i, wood in enumerate(VANILLA_WOOD):
        lang.write("""  "block.waxedwood.waxed_""" + wood + """_planks": "waxed """ + wood.title().replace("_", " ") + """ Planks",""")
        lang.write("""  "block.waxedwood.waxed_""" + wood + """_stairs": "waxed """ + wood.title().replace("_", " ") + """ Stairs",""")
        lang.write("""  "block.waxedwood.waxed_""" + wood + """_slab": "waxed """ + wood.title().replace("_", " ") + """ Slab",""")
        lang.write("""  "block.waxedwood.waxed_""" + wood + """_fence_gate": "waxed """ + wood.title().replace("_", " ") + """ Fence Gate",""")
        lang.write("""  "block.waxedwood.waxed_""" + wood + """_fence": "waxed """ + wood.title().replace("_", " ") + """ Fence",""")
        lang.write("""  "block.waxedwood.waxed_""" + wood + """_log": "waxed """ + wood.title().replace("_", " ") + """ Log",""")
        lang.write("""  "block.waxedwood.waxed_stripped_""" + wood + """_log": "waxed Stripped """ + wood.title().replace("_", " ") + """ Log",""")
        lang.write("""  "block.waxedwood.waxed_""" + wood + """_wood": "waxed """ + wood.title().replace("_", " ") + """ Wood",""")
        lang.write("""  "block.waxedwood.waxed_stripped_""" + wood + """_wood": "waxed Stripped """ + wood.title().replace("_", " ") + """ Wood\"""")
        if i != len(VANILLA_WOOD) - 1:
            lang.write(",")
        lang.write("\n")
    lang.write("}")

with open(path.join(tags_dir, "planks.json"), "w") as tags:
    tags.write("""{
  "replace": false,
  "values": [\n""")
    for i, wood in enumerate(VANILLA_WOOD):
        tags.write("    \"waxedwood:waxed_" + wood + "_planks\"")
        if i != len(VANILLA_WOOD) - 1:
            tags.write(",")
        tags.write("\n")
    tags.write("  ]\n}")

with open(path.join(tags_dir, "wooden_stairs.json"), "w") as tags:
    tags.write("""{
  "replace": false,
  "values": [\n""")
    for i, wood in enumerate(VANILLA_WOOD):
        tags.write("    \"waxedwood:waxed_" + wood + "_stairs\"")
        if i != len(VANILLA_WOOD) - 1:
            tags.write(",")
        tags.write("\n")
    tags.write("  ]\n}")
    # Note we don't need to add "stairs" tag, since it already includes wooden_stairs tag

with open(path.join(tags_dir, "wooden_slabs.json"), "w") as tags:
    tags.write("""{
  "replace": false,
  "values": [\n""")
    for i, wood in enumerate(VANILLA_WOOD):
        tags.write("    \"waxedwood:waxed_" + wood + "_slab\"")
        if i != len(VANILLA_WOOD) - 1:
            tags.write(",")
        tags.write("\n")
    tags.write("  ]\n}")
    # Note we don't need to add "slabs" tag, since it already includes wooden_slabs tag

with open(path.join(tags_dir, "fence_gates.json"), "w") as tags:
    tags.write("""{
  "replace": false,
  "values": [\n""")
    for i, wood in enumerate(VANILLA_WOOD):
        tags.write("    \"waxedwood:waxed_" + wood + "_fence_gate\"")
        if i != len(VANILLA_WOOD) - 1:
            tags.write(",")
        tags.write("\n")
    tags.write("  ]\n}")

with open(path.join(tags_dir, "fences.json"), "w") as tags:
    tags.write("""{
  "replace": false,
  "values": [\n""")
    for i, wood in enumerate(VANILLA_WOOD):
        tags.write("    \"waxedwood:waxed_" + wood + "_fence\"")
        if i != len(VANILLA_WOOD) - 1:
            tags.write(",")
        tags.write("\n")
    tags.write("  ]\n}")

with open(path.join(tags_dir, "logs.json"), "w") as tags:
    tags.write("""{
  "replace": false,
  "values": [\n""")
    for i, wood in enumerate(VANILLA_WOOD):
        tags.write("    \"waxedwood:waxed_" + wood + "_log\"")
        if i != len(VANILLA_WOOD) - 1:
            tags.write(",")
        tags.write("\n")
    tags.write("  ]\n}")

with open(path.join(tags_dir, "non_flammable_wood.json"), "w") as tags:
    tags.write("""{
  "replace": false,
  "values": [\n""")
    for i, wood in enumerate(VANILLA_WOOD):
        tags.write("    \"waxedwood:waxed_" + wood + "_planks\",\n")
        tags.write("    \"waxedwood:waxed_" + wood + "_stairs\",\n")
        tags.write("    \"waxedwood:waxed_" + wood + "_slab\",\n")
        tags.write("    \"waxedwood:waxed_" + wood + "_fence_gate\",\n")
        tags.write("    \"waxedwood:waxed_" + wood + "_fence\",\n")
        tags.write("    \"waxedwood:waxed_" + wood + "_log\",\n")
        tags.write("    \"waxedwood:waxed_stripped_" + wood + "_log\",\n")
        tags.write("    \"waxedwood:waxed_" + wood + "_wood\",\n")
        tags.write("    \"waxedwood:waxed_stripped_" + wood + "_wood\"")
        if i != len(VANILLA_WOOD) - 1:
            tags.write(",")
        tags.write("\n")
    tags.write("  ]\n}")
