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

assert path.exists(path.join(os.getcwd(), "make_waxedwood_resource_files.py")), "Not in correct directory"

resources_dir = path.join(os.getcwd(), "src", "main", "resources")
block_model_dir = path.join(resources_dir, "assets", "waxedwood", "models", "block")
item_models_dir = path.join(resources_dir, "assets", "waxedwood", "models", "item")
block_states_dir = path.join(resources_dir, "assets", "waxedwood", "blockstates")
lang_file = path.join(resources_dir, "assets", "waxedwood", "lang", "en_us.json")
block_loot_tables_dir = path.join(resources_dir, "data", "waxedwood", "loot_tables", "blocks")
recipes_dir = path.join(resources_dir, "data", "waxedwood", "recipes")
block_tags_dir = path.join(resources_dir, "data", "minecraft", "tags", "blocks")
    # "minecraft" for tags instead of "waxedwood", so we add to vanilla's tags eg minecraft:planks
item_tags_dir = path.join(resources_dir, "data", "minecraft", "tags", "items")

def item_model_for(name):
    return f"""{{
  "parent": "waxedwood:block/{name}\"
}}"""

def loot_table_for(name):
    return f"""{{
  "type": "minecraft:block",
  "pools": [
    {{
      "rolls": 1,
      "entries": [
        {{
          "type": "minecraft:item",
          "name": "waxedwood:{name}"
        }}
      ],
      "conditions": [
        {{
          "condition": "minecraft:survives_explosion"
        }}
      ]
    }}
  ]
}}"""

def block_states_for_planks(wood):
    return f"""{{
  "variants": {{
    "": {{
      "model": "waxedwood:block/waxed_{wood}_planks"
    }}
  }}
}}"""

def block_states_for_stairs(wood):
    return f"""{{
  "variants": {{
    "facing=east,half=bottom,shape=inner_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner",
      "y": 270,
      "uvlock": true
    }},
    "facing=east,half=bottom,shape=inner_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner"
    }},
    "facing=east,half=bottom,shape=outer_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer",
      "y": 270,
      "uvlock": true
    }},
    "facing=east,half=bottom,shape=outer_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer"
    }},
    "facing=east,half=bottom,shape=straight": {{
      "model": "waxedwood:block/waxed_{wood}_stairs"
    }},
    "facing=east,half=top,shape=inner_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner",
      "x": 180,
      "uvlock": true
    }},
    "facing=east,half=top,shape=inner_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner",
      "x": 180,
      "y": 90,
      "uvlock": true
    }},
    "facing=east,half=top,shape=outer_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer",
      "x": 180,
      "uvlock": true
    }},
    "facing=east,half=top,shape=outer_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer",
      "x": 180,
      "y": 90,
      "uvlock": true
    }},
    "facing=east,half=top,shape=straight": {{
      "model": "waxedwood:block/waxed_{wood}_stairs",
      "x": 180,
      "uvlock": true
    }},
    "facing=north,half=bottom,shape=inner_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner",
      "y": 180,
      "uvlock": true
    }},
    "facing=north,half=bottom,shape=inner_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner",
      "y": 270,
      "uvlock": true
    }},
    "facing=north,half=bottom,shape=outer_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer",
      "y": 180,
      "uvlock": true
    }},
    "facing=north,half=bottom,shape=outer_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer",
      "y": 270,
      "uvlock": true
    }},
    "facing=north,half=bottom,shape=straight": {{
      "model": "waxedwood:block/waxed_{wood}_stairs",
      "y": 270,
      "uvlock": true
    }},
    "facing=north,half=top,shape=inner_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner",
      "x": 180,
      "y": 270,
      "uvlock": true
    }},
    "facing=north,half=top,shape=inner_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner",
      "x": 180,
      "uvlock": true
    }},
    "facing=north,half=top,shape=outer_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer",
      "x": 180,
      "y": 270,
      "uvlock": true
    }},
    "facing=north,half=top,shape=outer_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer",
      "x": 180,
      "uvlock": true
    }},
    "facing=north,half=top,shape=straight": {{
      "model": "waxedwood:block/waxed_{wood}_stairs",
      "x": 180,
      "y": 270,
      "uvlock": true
    }},
    "facing=south,half=bottom,shape=inner_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner"
    }},
    "facing=south,half=bottom,shape=inner_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner",
      "y": 90,
      "uvlock": true
    }},
    "facing=south,half=bottom,shape=outer_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer"
    }},
    "facing=south,half=bottom,shape=outer_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer",
      "y": 90,
      "uvlock": true
    }},
    "facing=south,half=bottom,shape=straight": {{
      "model": "waxedwood:block/waxed_{wood}_stairs",
      "y": 90,
      "uvlock": true
    }},
    "facing=south,half=top,shape=inner_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner",
      "x": 180,
      "y": 90,
      "uvlock": true
    }},
    "facing=south,half=top,shape=inner_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner",
      "x": 180,
      "y": 180,
      "uvlock": true
    }},
    "facing=south,half=top,shape=outer_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer",
      "x": 180,
      "y": 90,
      "uvlock": true
    }},
    "facing=south,half=top,shape=outer_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer",
      "x": 180,
      "y": 180,
      "uvlock": true
    }},
    "facing=south,half=top,shape=straight": {{
      "model": "waxedwood:block/waxed_{wood}_stairs",
      "x": 180,
      "y": 90,
      "uvlock": true
    }},
    "facing=west,half=bottom,shape=inner_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner",
      "y": 90,
      "uvlock": true
    }},
    "facing=west,half=bottom,shape=inner_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner",
      "y": 180,
      "uvlock": true
    }},
    "facing=west,half=bottom,shape=outer_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer",
      "y": 90,
      "uvlock": true
    }},
    "facing=west,half=bottom,shape=outer_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer",
      "y": 180,
      "uvlock": true
    }},
    "facing=west,half=bottom,shape=straight": {{
      "model": "waxedwood:block/waxed_{wood}_stairs",
      "y": 180,
      "uvlock": true
    }},
    "facing=west,half=top,shape=inner_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner",
      "x": 180,
      "y": 180,
      "uvlock": true
    }},
    "facing=west,half=top,shape=inner_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_inner",
      "x": 180,
      "y": 270,
      "uvlock": true
    }},
    "facing=west,half=top,shape=outer_left": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer",
      "x": 180,
      "y": 180,
      "uvlock": true
    }},
    "facing=west,half=top,shape=outer_right": {{
      "model": "waxedwood:block/waxed_{wood}_stairs_outer",
      "x": 180,
      "y": 270,
      "uvlock": true
    }},
    "facing=west,half=top,shape=straight": {{
      "model": "waxedwood:block/waxed_{wood}_stairs",
      "x": 180,
      "y": 180,
      "uvlock": true
    }}
  }}
}}"""

def block_states_for_slab(wood):
    return f"""{{
  "variants": {{
    "type=bottom": {{
      "model": "waxedwood:block/waxed_{wood}_slab"
    }},
    "type=double": {{
      "model": "waxedwood:block/waxed_{wood}_planks"
    }},
    "type=top": {{
      "model": "waxedwood:block/waxed_{wood}_slab_top"
    }}
  }}
}}"""

def block_states_for_gate(wood):
    return f"""{{
  "variants": {{
    "facing=east,in_wall=false,open=false": {{
      "uvlock": true,
      "y": 270,
      "model": "waxedwood:block/waxed_{wood}_fence_gate"
    }},
    "facing=east,in_wall=false,open=true": {{
      "uvlock": true,
      "y": 270,
      "model": "waxedwood:block/waxed_{wood}_fence_gate_open"
    }},
    "facing=east,in_wall=true,open=false": {{
      "uvlock": true,
      "y": 270,
      "model": "waxedwood:block/waxed_{wood}_fence_gate_wall"
    }},
    "facing=east,in_wall=true,open=true": {{
      "uvlock": true,
      "y": 270,
      "model": "waxedwood:block/waxed_{wood}_fence_gate_wall_open"
    }},
    "facing=north,in_wall=false,open=false": {{
      "uvlock": true,
      "y": 180,
      "model": "waxedwood:block/waxed_{wood}_fence_gate"
    }},
    "facing=north,in_wall=false,open=true": {{
      "uvlock": true,
      "y": 180,
      "model": "waxedwood:block/waxed_{wood}_fence_gate_open"
    }},
    "facing=north,in_wall=true,open=false": {{
      "uvlock": true,
      "y": 180,
      "model": "waxedwood:block/waxed_{wood}_fence_gate_wall"
    }},
    "facing=north,in_wall=true,open=true": {{
      "uvlock": true,
      "y": 180,
      "model": "waxedwood:block/waxed_{wood}_fence_gate_wall_open"
    }},
    "facing=south,in_wall=false,open=false": {{
      "uvlock": true,
      "model": "waxedwood:block/waxed_{wood}_fence_gate"
    }},
    "facing=south,in_wall=false,open=true": {{
      "uvlock": true,
      "model": "waxedwood:block/waxed_{wood}_fence_gate_open"
    }},
    "facing=south,in_wall=true,open=false": {{
      "uvlock": true,
      "model": "waxedwood:block/waxed_{wood}_fence_gate_wall"
    }},
    "facing=south,in_wall=true,open=true": {{
      "uvlock": true,
      "model": "waxedwood:block/waxed_{wood}_fence_gate_wall_open"
    }},
    "facing=west,in_wall=false,open=false": {{
      "uvlock": true,
      "y": 90,
      "model": "waxedwood:block/waxed_{wood}_fence_gate"
    }},
    "facing=west,in_wall=false,open=true": {{
      "uvlock": true,
      "y": 90,
      "model": "waxedwood:block/waxed_{wood}_fence_gate_open"
    }},
    "facing=west,in_wall=true,open=false": {{
      "uvlock": true,
      "y": 90,
      "model": "waxedwood:block/waxed_{wood}_fence_gate_wall"
    }},
    "facing=west,in_wall=true,open=true": {{
      "uvlock": true,
      "y": 90,
      "model": "waxedwood:block/waxed_{wood}_fence_gate_wall_open"
    }}
  }}
}}"""

def block_states_for_fence(wood):
    return f"""{{
  "multipart": [
    {{
      "apply": {{
        "model": "waxedwood:block/waxed_{wood}_fence_post"
      }}
    }},
    {{
      "when": {{
        "north": "true"
      }},
      "apply": {{
        "model": "waxedwood:block/waxed_{wood}_fence_side",
        "uvlock": true
      }}
    }},
    {{
      "when": {{
        "east": "true"
      }},
      "apply": {{
        "model": "waxedwood:block/waxed_{wood}_fence_side",
        "y": 90,
        "uvlock": true
      }}
    }},
    {{
      "when": {{
        "south": "true"
      }},
      "apply": {{
        "model": "waxedwood:block/waxed_{wood}_fence_side",
        "y": 180,
        "uvlock": true
      }}
    }},
    {{
      "when": {{
        "west": "true"
      }},
      "apply": {{
        "model": "waxedwood:block/waxed_{wood}_fence_side",
        "y": 270,
        "uvlock": true
      }}
    }}
  ]
}}"""

def block_states_for_pillar_log(name):
    return f"""{{
  "variants": {{
    "axis=x": {{
      "model": "waxedwood:block/waxed_{name}_horizontal",
      "x": 90,
      "y": 90
    }},
    "axis=y": {{
      "model": "waxedwood:block/waxed_{name}"
    }},
    "axis=z": {{
      "model": "waxedwood:block/waxed_{name}_horizontal",
      "x": 90
    }}
  }}
}}"""
block_states_for_log = lambda wood: block_states_for_pillar_log(f"{wood}_log")
block_states_for_stripped_log = lambda wood: block_states_for_pillar_log(f"stripped_{wood}_log")

def block_states_for_pillar_wood(name):
    return f"""{{
  "variants": {{
    "axis=x": {{
      "model": "waxedwood:block/waxed_{name}",
      "x": 90,
      "y": 90
    }},
    "axis=y": {{
      "model": "waxedwood:block/waxed_{name}"
    }},
    "axis=z": {{
      "model": "waxedwood:block/waxed_{name}",
      "x": 90
    }}
  }}
}}"""
block_states_for_wood = lambda wood: block_states_for_pillar_wood(f"{wood}_wood")
block_states_for_stripped_wood = lambda wood: block_states_for_pillar_wood(f"stripped_{wood}_wood")

def block_model_for_planks(wood):
    return f"""{{
  "parent": "minecraft:block/cube_all",
  "textures": {{
    "all": "waxedwood:block/waxed_{wood}_planks"
  }}
}}"""

def block_model_bottom_top_side(wood, parent):
    return f"""{{
  "parent": "minecraft:block/{parent}",
  "textures": {{
    "bottom": "waxedwood:block/waxed_{wood}_planks",
    "top": "waxedwood:block/waxed_{wood}_planks",
    "side": "waxedwood:block/waxed_{wood}_planks"
  }}
}}"""
block_model_for_stairs = lambda wood: block_model_bottom_top_side(wood, "stairs")
block_model_for_stairs_inner = lambda wood: block_model_bottom_top_side(wood, "inner_stairs")
block_model_for_stairs_outer = lambda wood: block_model_bottom_top_side(wood, "outer_stairs")
block_model_for_slab = lambda wood: block_model_bottom_top_side(wood, "slab")
block_model_for_slab_top = lambda wood: block_model_bottom_top_side(wood, "slab_top")

def block_model_basic(wood, parent):
    return f"""{{
  "parent": "minecraft:block/{parent}",
  "textures": {{
    "texture": "waxedwood:block/waxed_{wood}_planks"
  }}
}}"""
block_model_for_gate = lambda wood: block_model_basic(wood, "template_fence_gate")
block_model_for_gate_open = lambda wood: block_model_basic(wood, "template_fence_gate_open")
block_model_for_gate_wall = lambda wood: block_model_basic(wood, "template_fence_gate_wall")
block_model_for_gate_wall_open = lambda wood: block_model_basic(wood, "template_fence_gate_wall_open")
block_model_for_fence_inventory = lambda wood: block_model_basic(wood, "fence_inventory")
block_model_for_fence_post = lambda wood: block_model_basic(wood, "fence_post")
block_model_for_fence_side = lambda wood: block_model_basic(wood, "fence_side")

def block_model_end_side(name, parent):
    return f"""{{
  "parent": "minecraft:block/{parent}",
  "textures": {{
    "end": "waxedwood:block/waxed_{name}_top",
    "side": "waxedwood:block/waxed_{name}"
  }}
}}"""
block_model_for_log = lambda wood: block_model_end_side(f"{wood}_log", "cube_column")
block_model_for_log_horizontal = lambda wood: block_model_end_side(f"{wood}_log", "cube_column_horizontal")
block_model_for_stripped_log = lambda wood: block_model_end_side(f"stripped_{wood}_log", "cube_column")
block_model_for_stripped_log_horizontal = lambda wood: block_model_end_side(f"stripped_{wood}_log", "cube_column_horizontal")

def block_model_end_side_equal(name, parent):
    return f"""{{
  "parent": "minecraft:block/{parent}",
  "textures": {{
    "end": "waxedwood:block/waxed_{name}",
    "side": "waxedwood:block/waxed_{name}"
  }}
}}"""
block_model_for_wood = lambda wood: block_model_end_side_equal(f"{wood}_log", "cube_column")
block_model_for_stripped_wood = lambda wood: block_model_end_side_equal(f"stripped_{wood}_log", "cube_column")

def write_planks_resources(wood):
    with open(path.join(item_models_dir, f"waxed_{wood}_planks.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(f"waxed_{wood}_planks"))
    with open(path.join(block_loot_tables_dir, f"waxed_{wood}_planks.json"), "w") as loot:
        loot.write(loot_table_for(f"waxed_{wood}_planks"))

    with open(path.join(block_states_dir, f"waxed_{wood}_planks.json"), "w") as blockstates:
        blockstates.write(block_states_for_planks(wood))

    with open(path.join(block_model_dir, f"waxed_{wood}_planks.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_planks(wood))

def write_stairs_resources(wood):
    with open(path.join(item_models_dir, f"waxed_{wood}_stairs.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(f"waxed_{wood}_stairs"))
    with open(path.join(block_loot_tables_dir, f"waxed_{wood}_stairs.json"), "w") as loot:
        loot.write(loot_table_for(f"waxed_{wood}_stairs"))

    with open(path.join(block_states_dir, f"waxed_{wood}_stairs.json"), "w") as blockstates:
        blockstates.write(block_states_for_stairs(wood))

    with open(path.join(block_model_dir, f"waxed_{wood}_stairs.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_stairs(wood))
    with open(path.join(block_model_dir, f"waxed_{wood}_stairs_inner.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_stairs_inner(wood))
    with open(path.join(block_model_dir, f"waxed_{wood}_stairs_outer.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_stairs_outer(wood))

def write_slab_resources(wood):
    with open(path.join(item_models_dir, f"waxed_{wood}_slab.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(f"waxed_{wood}_slab"))
    with open(path.join(block_loot_tables_dir, f"waxed_{wood}_slab.json"), "w") as loot:
        loot.write(loot_table_for(f"waxed_{wood}_slab"))

    with open(path.join(block_states_dir, f"waxed_{wood}_slab.json"), "w") as blockstates:
        blockstates.write(block_states_for_slab(wood))

    with open(path.join(block_model_dir, f"waxed_{wood}_slab.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_slab(wood))
    with open(path.join(block_model_dir, f"waxed_{wood}_slab_top.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_slab_top(wood))

def write_gate_resources(wood):
    with open(path.join(item_models_dir, f"waxed_{wood}_fence_gate.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(f"waxed_{wood}_fence_gate"))
    with open(path.join(block_loot_tables_dir, f"waxed_{wood}_fence_gate.json"), "w") as loot:
        loot.write(loot_table_for(f"waxed_{wood}_fence_gate"))

    with open(path.join(block_states_dir, f"waxed_{wood}_fence_gate.json"), "w") as blockstates:
        blockstates.write(block_states_for_gate(wood))

    with open(path.join(block_model_dir, f"waxed_{wood}_fence_gate.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_gate(wood))
    with open(path.join(block_model_dir, f"waxed_{wood}_fence_gate_open.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_gate_open(wood))
    with open(path.join(block_model_dir, f"waxed_{wood}_fence_gate_wall.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_gate_wall(wood))
    with open(path.join(block_model_dir, f"waxed_{wood}_fence_gate_wall_open.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_gate_wall_open(wood))

def write_fence_resources(wood):
    with open(path.join(item_models_dir, f"waxed_{wood}_fence.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(f"waxed_{wood}_fence_inventory")) # Note using a different model for item
    with open(path.join(block_loot_tables_dir, f"waxed_{wood}_fence.json"), "w") as loot:
        loot.write(loot_table_for(f"waxed_{wood}_fence"))

    with open(path.join(block_states_dir, f"waxed_{wood}_fence.json"), "w") as blockstates:
        blockstates.write(block_states_for_fence(wood))

    with open(path.join(block_model_dir, f"waxed_{wood}_fence_inventory.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_fence_inventory(wood))
    with open(path.join(block_model_dir, f"waxed_{wood}_fence_post.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_fence_post(wood))
    with open(path.join(block_model_dir, f"waxed_{wood}_fence_side.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_fence_side(wood))

def write_log_resources(wood):
    with open(path.join(item_models_dir, f"waxed_{wood}_log.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(f"waxed_{wood}_log"))
    with open(path.join(block_loot_tables_dir, f"waxed_{wood}_log.json"), "w") as loot:
        loot.write(loot_table_for(f"waxed_{wood}_log"))

    with open(path.join(block_states_dir, f"waxed_{wood}_log.json"), "w") as blockstates:
        blockstates.write(block_states_for_log(wood))

    with open(path.join(block_model_dir, f"waxed_{wood}_log.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_log(wood))
    with open(path.join(block_model_dir, f"waxed_{wood}_log_horizontal.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_log_horizontal(wood))

def write_stripped_log_resources(wood):
    with open(path.join(item_models_dir, f"waxed_stripped_{wood}_log.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(f"waxed_stripped_{wood}_log"))
    with open(path.join(block_loot_tables_dir, f"waxed_stripped_{wood}_log.json"), "w") as loot:
        loot.write(loot_table_for(f"waxed_stripped_{wood}_log"))

    with open(path.join(block_states_dir, f"waxed_stripped_{wood}_log.json"), "w") as blockstates:
        blockstates.write(block_states_for_stripped_log(wood))

    with open(path.join(block_model_dir, f"waxed_stripped_{wood}_log.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_stripped_log(wood))
    with open(path.join(block_model_dir, f"waxed_stripped_{wood}_log_horizontal.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_stripped_log_horizontal(wood))

def write_wood_resources(wood):
    with open(path.join(item_models_dir, f"waxed_{wood}_wood.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(f"waxed_{wood}_wood"))
    with open(path.join(block_loot_tables_dir, f"waxed_{wood}_wood.json"), "w") as loot:
        loot.write(loot_table_for(f"waxed_{wood}_wood"))

    with open(path.join(block_states_dir, f"waxed_{wood}_wood.json"), "w") as blockstates:
        blockstates.write(block_states_for_wood(wood))

    with open(path.join(block_model_dir, f"waxed_{wood}_wood.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_wood(wood))

def write_stripped_wood_resources(wood):
    with open(path.join(item_models_dir, f"waxed_stripped_{wood}_wood.json"), "w") as itemmodel:
        itemmodel.write(item_model_for(f"waxed_stripped_{wood}_wood"))
    with open(path.join(block_loot_tables_dir, f"waxed_stripped_{wood}_wood.json"), "w") as loot:
        loot.write(loot_table_for(f"waxed_stripped_{wood}_wood"))

    with open(path.join(block_states_dir, f"waxed_stripped_{wood}_wood.json"), "w") as blockstates:
        blockstates.write(block_states_for_stripped_wood(wood))

    with open(path.join(block_model_dir, f"waxed_stripped_{wood}_wood.json"), "w") as blockmodel:
        blockmodel.write(block_model_for_stripped_wood(wood))

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


# NAMES
########################################################################

with open(lang_file, "w") as lang:
    lang.write("{\n")
    for i, wood in enumerate(VANILLA_WOOD):
        lang.write(f"""  "block.waxedwood.waxed_{wood}_planks": "Waxed {wood.title().replace("_", " ")} Planks",""")
        lang.write(f"""  "block.waxedwood.waxed_{wood}_stairs": "Waxed {wood.title().replace("_", " ")} Stairs",""")
        lang.write(f"""  "block.waxedwood.waxed_{wood}_slab": "Waxed {wood.title().replace("_", " ")} Slab",""")
        lang.write(f"""  "block.waxedwood.waxed_{wood}_fence_gate": "Waxed {wood.title().replace("_", " ")} Fence Gate",""")
        lang.write(f"""  "block.waxedwood.waxed_{wood}_fence": "Waxed {wood.title().replace("_", " ")} Fence",""")
        lang.write(f"""  "block.waxedwood.waxed_{wood}_log": "Waxed {wood.title().replace("_", " ")} Log",""")
        lang.write(f"""  "block.waxedwood.waxed_stripped_{wood}_log": "Waxed Stripped {wood.title().replace("_", " ")} Log",""")
        lang.write(f"""  "block.waxedwood.waxed_{wood}_wood": "Waxed {wood.title().replace("_", " ")} Wood",""")
        lang.write(f"""  "block.waxedwood.waxed_stripped_{wood}_wood": "Waxed Stripped {wood.title().replace("_", " ")} Wood\"""")
        if i != len(VANILLA_WOOD) - 1:
            lang.write(",")
        lang.write("\n")
    lang.write("}")


# TAGS
########################################################################

def make_tags(fname, namefunc, tags_dir=None):
    if tags_dir is None:
        make_tags(fname, namefunc, block_tags_dir)
        make_tags(fname, namefunc, item_tags_dir)
        return
    with open(path.join(tags_dir, f"{fname}.json"), "w") as tags:
        tags.write(f"""{{
  "replace": false,
  "values": [\n""")
        for i, wood in enumerate(VANILLA_WOOD):
            name = namefunc(wood)
            tags.write(f"    \"waxedwood:waxed_{name}\"")
            if i != len(VANILLA_WOOD) - 1:
                tags.write(",")
            tags.write("\n")
        tags.write("  ]\n}")

make_tags("planks", lambda wood: f"{wood}_planks")
make_tags("wooden_stairs", lambda wood: f"{wood}_stairs")
    # Note we don't need to add "stairs" tag, since it already includes wooden_stairs tag
make_tags("wooden_slabs", lambda wood: f"{wood}_slab")
    # Note we don't need to add "slabs" tag, since it already includes wooden_slabs tag
make_tags("fence_gates", lambda wood: f"{wood}_fence_gate", block_tags_dir)
make_tags("fences", lambda wood: f"{wood}_fence")
make_tags("logs", lambda wood: f"{wood}_log")

for tags_dir in (block_tags_dir, item_tags_dir):
    with open(path.join(tags_dir, "non_flammable_wood.json"), "w") as tags:
        tags.write(f"""{{
      "replace": false,
      "values": [\n""")
        for i, wood in enumerate(VANILLA_WOOD):
            tags.write(f"    \"waxedwood:waxed_{wood}_planks\",\n")
            tags.write(f"    \"waxedwood:waxed_{wood}_stairs\",\n")
            tags.write(f"    \"waxedwood:waxed_{wood}_slab\",\n")
            tags.write(f"    \"waxedwood:waxed_{wood}_fence_gate\",\n")
            tags.write(f"    \"waxedwood:waxed_{wood}_fence\",\n")
            tags.write(f"    \"waxedwood:waxed_{wood}_log\",\n")
            tags.write(f"    \"waxedwood:waxed_stripped_{wood}_log\",\n")
            tags.write(f"    \"waxedwood:waxed_{wood}_wood\",\n")
            tags.write(f"    \"waxedwood:waxed_stripped_{wood}_wood\"")
            if i != len(VANILLA_WOOD) - 1:
                tags.write(",")
            tags.write("\n")
        tags.write("  ]\n}")


# RECIPES
########################################################################

def recipe_for_waxed(name):
    return f"""{{
  "type": "minecraft:crafting_shapeless",
  "ingredients": [
    {{
      "item": "minecraft:{name}"
    }},
    {{
      "item": "minecraft:honeycomb"
    }}
  ],
  "result": {{
    "item": "waxedwood:waxed_{name}"
  }}
}}"""

def recipe_for_removing_wax(name):
    return f"""{{
  "type": "minecraft:crafting_shapeless",
  "ingredients": [
    {{
      "item": "waxedwood:waxed_{name}"
    }}
  ],
  "result": {{
    "item": "minecraft:{name}"
  }}
}}"""

def make_basic_recipes_for(name):
    with open(path.join(recipes_dir, f"{name}.json"), "w") as f:
        f.write(recipe_for_removing_wax(name))
    with open(path.join(recipes_dir, f"waxed_{name}.json"), "w") as f:
        f.write(recipe_for_waxed(name))

def make_logs_plank_recipe(wood):
    with open(path.join(recipes_dir, f"waxed_{wood}_planks.json"), "w") as f:
        f.write(f"""{{
  "type": "minecraft:crafting_shapeless",
  "ingredients": [
    {{
      "item": "waxedwood:waxed_{wood}_log"
    }}
  ],
  "result": {{
    "item": "minecraft:{wood}_planks",
    "amount": 4
  }}
}}""")

def make_stairs_recipe(wood):
    with open(path.join(recipes_dir, f"waxed_{wood}_stairs.json"), "w") as f:
        f.write(f"""{{
  "type": "minecraft:crafting_shaped",
  "group": "wooden_stairs",
  "pattern": [
    "#  ",
    "## ",
    "###"
  ],
  "key": {{
    "#": {{
      "item": "waxedwood:waxed_{wood}_planks"
    }}
  }},
  "result": {{
    "item": "waxedwood:waxed_{wood}_stairs",
    "count": 4
  }}
}}""")

def make_slab_recipe(wood):
    with open(path.join(recipes_dir, f"waxed_{wood}_slab.json"), "w") as f:
        f.write(f"""{{
  "type": "minecraft:crafting_shaped",
  "group": "wooden_slab",
  "pattern": [
    "###"
  ],
  "key": {{
    "#": {{
      "item": "waxedwood:waxed_{wood}_planks"
    }}
  }},
  "result": {{
    "item": "waxedwood:waxed_{wood}_slab",
    "count": 6
  }}
}}""")

def make_fence_gate_recipe(wood):
    with open(path.join(recipes_dir, f"waxed_{wood}_fence_gate.json"), "w") as f:
        f.write(f"""{{
  "type": "minecraft:crafting_shaped",
  "group": "wooden_fence_gate",
  "pattern": [
    "#W#",
    "#W#"
  ],
  "key": {{
    "#": {{
      "item": "minecraft:stick"
    }},
    "W": {{
      "item": "waxedwood:waxed_{wood}_planks"
    }}
  }},
  "result": {{
    "item": "waxedwood:waxed_{wood}_fence_gate"
  }}
}}""")

def make_fence_recipe(wood):
    with open(path.join(recipes_dir, f"waxed_{wood}_fence.json"), "w") as f:
        f.write(f"""{{
  "type": "minecraft:crafting_shaped",
  "group": "wooden_fence",
  "pattern": [
    "W#W",
    "W#W"
  ],
  "key": {{
    "#": {{
      "item": "minecraft:stick"
    }},
    "W": {{
      "item": "waxedwood:waxed_{wood}_planks"
    }}
  }},
  "result": {{
    "item": "waxedwood:waxed_{wood}_fence",
    "count": 3
  }}
}}""")

def make_wood_recipe(wood):
    with open(path.join(recipes_dir, f"waxed_{wood}_wood.json"), "w") as f:
        f.write(f"""{{
  "type": "minecraft:crafting_shaped",
  "group": "bark",
  "pattern": [
    "##",
    "##"
  ],
  "key": {{
    "#": {{
      "item": "waxedwood:waxed_{wood}_log"
    }}
  }},
  "result": {{
    "item": "waxedwood:waxed_{wood}_wood",
    "count": 3
  }}
}}""")

def make_sign_recipe(wood):
    with open(path.join(recipes_dir, f"{wood}_sign.json"), "w") as f:
        f.write(f"""{{
  "type": "minecraft:crafting_shaped",
  "group": "sign",
  "pattern": [
    "###",
    "###",
    " X "
  ],
  "key": {{
    "#": {{
      "item": "waxedwood:waxed_{wood}_planks"
    }},
    "X": {{
      "item": "minecraft:stick"
    }}
  }},
  "result": {{
    "item": "minecraft:{wood}_sign",
    "count": 3
  }}
}}""")


def make_door_recipe(wood):
    with open(path.join(recipes_dir, f"{wood}_door.json"), "w") as f:
        f.write(f"""{{
  "type": "minecraft:crafting_shaped",
  "group": "wooden_door",
  "pattern": [
    "##",
    "##",
    "##"
  ],
  "key": {{
    "#": {{
      "item": "waxedwood:waxed_{wood}_planks"
    }}
  }},
  "result": {{
    "item": "minecraft:{wood}_door",
    "count": 3
  }}
}}""")

def make_trapdoor_recipe(wood):
    with open(path.join(recipes_dir, f"{wood}_trapdoor.json"), "w") as f:
        f.write(f"""{{
  "type": "minecraft:crafting_shaped",
  "group": "wooden_trapdoor",
  "pattern": [
    "###",
    "###"
  ],
  "key": {{
    "#": {{
      "item": "waxedwood:waxed_{wood}_planks"
    }}
  }},
  "result": {{
    "item": "minecraft:{wood}_trapdoor",
    "count": 2
  }}
}}""")

def make_button_recipe(wood):
    with open(path.join(recipes_dir, f"{wood}_button.json"), "w") as f:
        f.write(f"""{{
  "type": "minecraft:crafting_shapeless",
  "group": "wooden_button",
  "ingredients": [
    {{
      "item": "waxedwood:waxed_{wood}_planks"
    }}
  ],
  "result": {{
    "item": "minecraft:{wood}_button"
  }}
}}""")

def make_boat_recipe(wood):
    with open(path.join(recipes_dir, f"{wood}_boat.json"), "w") as f:
        f.write(f"""{{
  "type": "minecraft:crafting_shaped",
  "group": "boat",
  "pattern": [
    "# #",
    "###"
  ],
  "key": {{
    "#": {{
      "item": "waxedwood:waxed_{wood}_planks"
    }}
  }},
  "result": {{
    "item": "minecraft:{wood}_boat"
  }}
}}""")

def make_pressure_plate_recipe(wood):
    with open(path.join(recipes_dir, f"{wood}_pressure_plate.json"), "w") as f:
        f.write(f"""{{
  "type": "minecraft:crafting_shaped",
  "group": "wooden_pressure_plate",
  "pattern": [
    "##"
  ],
  "key": {{
    "#": {{
      "item": "waxedwood:waxed_{wood}_planks"
    }}
  }},
  "result": {{
    "item": "minecraft:{wood}_pressure_plate"
  }}
}}""")

for wood in VANILLA_WOOD:
    make_basic_recipes_for(f"{wood}_planks")
    make_basic_recipes_for(f"{wood}_stairs")
    make_basic_recipes_for(f"{wood}_slab")
    make_basic_recipes_for(f"{wood}_fence_gate")
    make_basic_recipes_for(f"{wood}_fence")
    make_basic_recipes_for(f"{wood}_log")
    make_basic_recipes_for(f"stripped_{wood}_log")
    make_basic_recipes_for(f"{wood}_wood")
    make_basic_recipes_for(f"stripped_{wood}_wood")
    make_logs_plank_recipe(wood)
    make_stairs_recipe(wood)
    make_slab_recipe(wood)
    make_fence_gate_recipe(wood)
    make_fence_recipe(wood)
    make_wood_recipe(wood)
    #make_stick_recipe(wood) -- not necessary, vanilla recipe is for tag "planks"
    make_sign_recipe(wood)
    make_door_recipe(wood)
    make_trapdoor_recipe(wood)
    make_boat_recipe(wood)
    make_button_recipe(wood)
    make_pressure_plate_recipe(wood)


# TEXTURES
########################################################################

if len(sys.argv) != 2:
    print("No minecraft resources dir given, skipping texture gen")
else:
    vanilla_dir = path.join(sys.argv[1], "assets", "minecraft", "textures", "block")
    waxed_dir = path.join(resources_dir, "assets", "waxedwood", "textures", "block")

    def copy_recolor(name):
        os.system(path.join(os.getcwd(), "colors", "curves") + " \"20,15 30,20 70,55 100,80\" \""
                + path.join(vanilla_dir, name + ".png") + "\" \"" + path.join(waxed_dir, "waxed_" + name + "_temp.png") + "\"")
        os.system(path.join(os.getcwd(), "colors", "colorbalance") + " -c r -a 5 \""
                + path.join(waxed_dir, "waxed_" + name + "_temp.png") + "\" \"" + path.join(waxed_dir, "waxed_" + name + ".png") + "\"")
        os.system("rm \"" + path.join(waxed_dir, "waxed_" + name + "_temp.png\""))

    for wood in VANILLA_WOOD:
        copy_recolor(f"{wood}_planks")
        copy_recolor(f"{wood}_log")
        copy_recolor(f"{wood}_log_top")
        copy_recolor(f"stripped_{wood}_log")
        copy_recolor(f"stripped_{wood}_log_top")
