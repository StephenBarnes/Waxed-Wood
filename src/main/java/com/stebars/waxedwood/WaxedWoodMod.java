package com.stebars.waxedwood;

import java.util.HashMap;
import java.util.Map;

import net.minecraft.block.AbstractBlock;
import net.minecraft.block.Block;
import net.minecraft.block.FenceBlock;
import net.minecraft.block.FenceGateBlock;
import net.minecraft.block.RotatedPillarBlock;
import net.minecraft.block.SlabBlock;
import net.minecraft.block.SoundType;
import net.minecraft.block.StairsBlock;
import net.minecraft.block.material.Material;
import net.minecraft.block.material.MaterialColor;
import net.minecraft.item.BlockItem;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroup;
import net.minecraft.state.Property;
import net.minecraft.state.properties.BlockStateProperties;
import net.minecraft.util.Direction;
import net.minecraft.util.ResourceLocation;
import net.minecraft.util.SoundEvent;
import net.minecraft.util.SoundEvents;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.common.ToolType;
import net.minecraftforge.event.RegistryEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;


@Mod(WaxedWoodMod.MOD_ID)
@Mod.EventBusSubscriber(bus = Mod.EventBusSubscriber.Bus.MOD)
public class WaxedWoodMod {
	public final static String MOD_ID = "waxedwood";

	public final static String[] VANILLA_WOOD = {
			"oak",
			"spruce",
			"birch",
			"jungle",
			"acacia",
			"dark_oak"
	};

	public final static Property[] PLANKS_PROPERTIES = { };
	public final static Property[] STAIRS_PROPERTIES = { BlockStateProperties.HORIZONTAL_FACING, BlockStateProperties.HALF, BlockStateProperties.STAIRS_SHAPE };
	public final static Property[] SLAB_PROPERTIES = { BlockStateProperties.SLAB_TYPE };
	public final static Property[] FENCE_PROPERTIES = {  };
	public final static Property[] GATE_PROPERTIES = { BlockStateProperties.HORIZONTAL_FACING, BlockStateProperties.IN_WALL, BlockStateProperties.OPEN };
	public final static Property[] LOG_PROPERTIES = { BlockStateProperties.AXIS };
	public final static Property[] STRIPPED_LOG_PROPERTIES = { BlockStateProperties.AXIS };
	public final static Property[] WOOD_PROPERTIES = { BlockStateProperties.AXIS };
	public final static Property[] STRIPPED_WOOD_PROPERTIES = { BlockStateProperties.AXIS };

	public static final Material WAXED_WOOD_MATERIAL = (new Material.Builder(MaterialColor.WOOD)).build();
	public static final SoundEvent WAXED_WOOD_STEP_SOUND = new SoundEvent(new ResourceLocation(WaxedWoodMod.MOD_ID, "waxedwoodstep"))
			.setRegistryName(new ResourceLocation(WaxedWoodMod.MOD_ID, "waxedwoodstep"));
	public static final SoundEvent WAXED_WOOD_BREAK_SOUND = new SoundEvent(new ResourceLocation(WaxedWoodMod.MOD_ID, "waxedwoodbreak"))
			.setRegistryName(new ResourceLocation(WaxedWoodMod.MOD_ID, "waxedwoodbreak"));
	public static final SoundType WAXED_WOOD_SOUND_TYPE = new SoundType(1.0F, 1.0F, WAXED_WOOD_BREAK_SOUND, WAXED_WOOD_STEP_SOUND,
			WAXED_WOOD_BREAK_SOUND, SoundEvents.WOOD_HIT, SoundEvents.WOOD_FALL);

	public static final Map<String, Block> PLANKS_BLOCKS = new HashMap<String, Block>();
	public static final Map<String, Block> STAIRS_BLOCKS = new HashMap<String, Block>();
	public static final Map<String, Block> SLAB_BLOCKS = new HashMap<String, Block>();
	public static final Map<String, Block> FENCE_BLOCKS = new HashMap<String, Block>();
	public static final Map<String, Block> GATE_BLOCKS = new HashMap<String, Block>();
	public static final Map<String, Block> LOG_BLOCKS = new HashMap<String, Block>();
	public static final Map<String, Block> STRIPPED_LOG_BLOCKS = new HashMap<String, Block>();
	public static final Map<String, Block> WOOD_BLOCKS = new HashMap<String, Block>();
	public static final Map<String, Block> STRIPPED_WOOD_BLOCKS = new HashMap<String, Block>();

	public static final Map<ResourceLocation, Block> ID_TO_WAXED_BLOCK = new HashMap<ResourceLocation, Block>();
	public static final Map<Block, Property[]> BLOCK_PROPERTIES = new HashMap<Block, Property[]>();
	public static final Map<Block, ResourceLocation> TOOL_MODIFIED = new HashMap<Block, ResourceLocation>();

	public WaxedWoodMod() {
		MinecraftForge.EVENT_BUS.register(this);
	}

	@SubscribeEvent
	public static void onSoundsRegistry(final RegistryEvent.Register<SoundEvent> event) {
		event.getRegistry().register(WAXED_WOOD_BREAK_SOUND);
	}

	@SubscribeEvent
	public static void onBlocksRegistry(final RegistryEvent.Register<Block> event) {
		for (String wood : VANILLA_WOOD) {
			final Block planks_block = new Block(
					AbstractBlock.Properties.of(WAXED_WOOD_MATERIAL, MaterialColor.WOOD)
					.strength(3.0F, 5.0F) // this is difficulty of mining and explosion resistance; vanilla wood is 2,3, stone is 1.5,6
					.harvestTool(ToolType.AXE)
					.sound(WAXED_WOOD_SOUND_TYPE))
					.setRegistryName(new ResourceLocation(MOD_ID, "waxed_" + wood + "_planks"));
			ID_TO_WAXED_BLOCK.put(new ResourceLocation("minecraft", wood + "_planks"), planks_block);
			BLOCK_PROPERTIES.put(planks_block, PLANKS_PROPERTIES);
			PLANKS_BLOCKS.put(wood, planks_block);

			@SuppressWarnings("deprecation") // vanilla code uses StairsBlock
			final Block stairs_block = new StairsBlock(
					planks_block.defaultBlockState(),
					AbstractBlock.Properties.copy(planks_block))
			.setRegistryName(new ResourceLocation(MOD_ID, "waxed_" + wood + "_stairs"));
			ID_TO_WAXED_BLOCK.put(new ResourceLocation("minecraft", wood + "_stairs"), stairs_block);
			BLOCK_PROPERTIES.put(stairs_block, STAIRS_PROPERTIES);
			STAIRS_BLOCKS.put(wood, stairs_block);

			final Block slab_block = new SlabBlock(
					AbstractBlock.Properties.copy(planks_block))
					.setRegistryName(new ResourceLocation(MOD_ID, "waxed_" + wood + "_slab"));
			ID_TO_WAXED_BLOCK.put(new ResourceLocation("minecraft", wood + "_slab"), slab_block);
			BLOCK_PROPERTIES.put(slab_block, SLAB_PROPERTIES);
			SLAB_BLOCKS.put(wood, slab_block);

			final Block gate_block = new FenceGateBlock(
					AbstractBlock.Properties.copy(planks_block))
					.setRegistryName(new ResourceLocation(MOD_ID, "waxed_" + wood + "_fence_gate"));
			ID_TO_WAXED_BLOCK.put(new ResourceLocation("minecraft", wood + "_fence_gate"), gate_block);
			BLOCK_PROPERTIES.put(gate_block, GATE_PROPERTIES);
			GATE_BLOCKS.put(wood, gate_block);

			final Block fence_block = new FenceBlock(
					AbstractBlock.Properties.copy(planks_block))
					.setRegistryName(new ResourceLocation(MOD_ID, "waxed_" + wood + "_fence"));
			ID_TO_WAXED_BLOCK.put(new ResourceLocation("minecraft", wood + "_fence"), fence_block);
			BLOCK_PROPERTIES.put(fence_block, FENCE_PROPERTIES);
			FENCE_BLOCKS.put(wood, fence_block);

			final Block log_block = new RotatedPillarBlock(AbstractBlock.Properties.of(WAXED_WOOD_MATERIAL,
					(p_235431_2_) -> {
						return p_235431_2_.getValue(RotatedPillarBlock.AXIS) == Direction.Axis.Y ? MaterialColor.WOOD : MaterialColor.PODZOL;
						// Colors here don't seem to actually do anything
					})
					.strength(3.0F, 5.0F)
					.sound(WAXED_WOOD_SOUND_TYPE)
					.harvestTool(ToolType.AXE))
					.setRegistryName(new ResourceLocation(MOD_ID, "waxed_" + wood + "_log"));
			ID_TO_WAXED_BLOCK.put(new ResourceLocation("minecraft", wood + "_log"), log_block);
			BLOCK_PROPERTIES.put(log_block, LOG_PROPERTIES);
			LOG_BLOCKS.put(wood, log_block);

			final Block stripped_log_block = new RotatedPillarBlock(AbstractBlock.Properties.of(WAXED_WOOD_MATERIAL,
					(p_235431_2_) -> {
						return p_235431_2_.getValue(RotatedPillarBlock.AXIS) == Direction.Axis.Y ? MaterialColor.PODZOL : MaterialColor.PODZOL;
						// TODO the colors are different for different types of wood
					})
					.strength(3.0F, 5.0F)
					.sound(WAXED_WOOD_SOUND_TYPE)
					.harvestTool(ToolType.AXE))
					.setRegistryName(new ResourceLocation(MOD_ID, "waxed_stripped_" + wood + "_log"));
			ID_TO_WAXED_BLOCK.put(new ResourceLocation("minecraft", "stripped_" + wood + "_log"), stripped_log_block);
			BLOCK_PROPERTIES.put(stripped_log_block, STRIPPED_LOG_PROPERTIES);
			STRIPPED_LOG_BLOCKS.put(wood, stripped_log_block);

			final Block wood_block = new RotatedPillarBlock(
					AbstractBlock.Properties.copy(planks_block)
					.strength(3.5F, 6.0F))
					.setRegistryName(new ResourceLocation(MOD_ID, "waxed_" + wood + "_wood"));
			ID_TO_WAXED_BLOCK.put(new ResourceLocation("minecraft", wood + "_wood"), wood_block);
			BLOCK_PROPERTIES.put(wood_block, WOOD_PROPERTIES);
			WOOD_BLOCKS.put(wood, wood_block);

			final Block stripped_wood_block = new RotatedPillarBlock(
					AbstractBlock.Properties.copy(planks_block)
					.strength(3.5F, 6.0F))
					.setRegistryName(new ResourceLocation(MOD_ID, "waxed_stripped_" + wood + "_wood"));
			ID_TO_WAXED_BLOCK.put(new ResourceLocation("minecraft", "stripped_" + wood + "_wood"), stripped_wood_block);
			BLOCK_PROPERTIES.put(stripped_wood_block, STRIPPED_WOOD_PROPERTIES);
			STRIPPED_WOOD_BLOCKS.put(wood, stripped_wood_block);

			TOOL_MODIFIED.put(log_block, new ResourceLocation("minecraft", "stripped_" + wood + "_log"));
			TOOL_MODIFIED.put(wood_block, new ResourceLocation("minecraft", "stripped_" + wood + "_wood"));

			event.getRegistry().registerAll(planks_block, stairs_block, slab_block, gate_block, fence_block,
					log_block, stripped_log_block, wood_block, stripped_wood_block);
		}
	}

	private static Item makeBlockItem(String id, Block block) {
		return new BlockItem(block,
				new Item.Properties().tab(ItemGroup.TAB_BUILDING_BLOCKS))
				.setRegistryName(new ResourceLocation(MOD_ID, id));
	}

	@SubscribeEvent
	public static void onItemsRegistry(final RegistryEvent.Register<Item> event) {
		for (String wood : VANILLA_WOOD) {
			event.getRegistry().registerAll(
					makeBlockItem("waxed_" + wood + "_planks", PLANKS_BLOCKS.get(wood)),
					makeBlockItem("waxed_" + wood + "_stairs", STAIRS_BLOCKS.get(wood)),
					makeBlockItem("waxed_" + wood + "_slab", SLAB_BLOCKS.get(wood)),
					makeBlockItem("waxed_" + wood + "_fence_gate", GATE_BLOCKS.get(wood)),
					makeBlockItem("waxed_" + wood + "_fence", FENCE_BLOCKS.get(wood)),
					makeBlockItem("waxed_" + wood + "_log", LOG_BLOCKS.get(wood)),
					makeBlockItem("waxed_stripped_" + wood + "_log", STRIPPED_LOG_BLOCKS.get(wood)),
					makeBlockItem("waxed_" + wood + "_wood", WOOD_BLOCKS.get(wood)),
					makeBlockItem("waxed_stripped_" + wood + "_wood", STRIPPED_WOOD_BLOCKS.get(wood))
					);
		}
	}

	// TODO fences connect+disconnect in a weird way with vanilla equivalents
}
