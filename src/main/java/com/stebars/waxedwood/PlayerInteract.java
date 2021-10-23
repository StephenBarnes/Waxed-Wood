package com.stebars.waxedwood;

import java.util.Random;

import net.minecraft.block.Block;
import net.minecraft.block.BlockState;
import net.minecraft.block.Blocks;
import net.minecraft.entity.player.PlayerEntity;
import net.minecraft.item.Items;
import net.minecraft.particles.BlockParticleData;
import net.minecraft.particles.ParticleTypes;
import net.minecraft.state.Property;
import net.minecraft.util.ResourceLocation;
import net.minecraft.util.SoundCategory;
import net.minecraft.util.SoundEvents;
import net.minecraft.util.math.BlockPos;
import net.minecraft.util.math.vector.Vector3d;
import net.minecraft.world.World;
import net.minecraftforge.common.ToolType;
import net.minecraftforge.event.entity.player.PlayerInteractEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod.EventBusSubscriber;
import net.minecraftforge.registries.ForgeRegistries;


@EventBusSubscriber
public class PlayerInteract {

	@SubscribeEvent
	public static void waxWood(final PlayerInteractEvent.RightClickBlock event) {
		if (!(event.getItemStack().getItem() == Items.HONEYCOMB))
			return;
		BlockState state = event.getWorld().getBlockState(event.getPos());
		Block block = state.getBlock();
		Block newBlock = WaxedWoodMod.ID_TO_WAXED_BLOCK.get(block.getRegistryName());
		if (newBlock == null)
			return;
		BlockPos pos = event.getPos();
		Vector3d centerPos = Vector3d.atCenterOf(pos);
		World world = event.getWorld();
		Random random = world.getRandom();

		// Copy over properties, so we don't change eg rotation of stairs
		BlockState newState = newBlock.defaultBlockState();
		/*for (Entry<Property<?>, Comparable<?>> property: blockstate.getValues().entrySet()) {
			replacementBlockState.setValue(property.getKey(), property.getValue());
		} -- this doesn't work*/
		for (Property property: WaxedWoodMod.BLOCK_PROPERTIES.get(newBlock)) {
			newState = newState.setValue(property, state.getValue(property));
		}

		world.playSound(event.getPlayer(), pos, SoundEvents.HONEY_BLOCK_SLIDE, SoundCategory.BLOCKS, .5F, 1F); // last args are volume, pitch
		world.setBlock(pos, newState, 3);
		if (!event.getPlayer().isCreative())
			event.getItemStack().shrink(1);

		for(int i = 0; i < 7; ++i) {
			world.addParticle(new BlockParticleData(ParticleTypes.BLOCK, Blocks.HONEY_BLOCK.defaultBlockState()),
					centerPos.x + random.nextFloat() - .5,
					centerPos.y + random.nextFloat() - .5,
					centerPos.z + random.nextFloat() - .5,
					0.0D, 0.0D, 0.0D);
		}

		event.setCanceled(true);
	}

	@SubscribeEvent
	public static void stripBlock(final PlayerInteractEvent.RightClickBlock event) {
		if (!event.getItemStack().getToolTypes().contains(ToolType.AXE))
			return;
		World world = event.getWorld();
		BlockPos pos = event.getPos();
		BlockState state = world.getBlockState(pos);
		Block block = state.getBlock();
		ResourceLocation newId = WaxedWoodMod.TOOL_MODIFIED.get(block);
		if (newId == null)
			return;
		Block newBlock = ForgeRegistries.BLOCKS.getValue(newId);
		BlockState newState =  newBlock.defaultBlockState();

		// Copy properties, so we don't rotate logs
		for (Property property: WaxedWoodMod.BLOCK_PROPERTIES.get(block)) {
			newState = newState.setValue(property, state.getValue(property));
		}

		PlayerEntity player = event.getPlayer();
		world.playSound(player, pos, SoundEvents.AXE_STRIP, SoundCategory.BLOCKS, 1.0F, 1.0F);
		if (!world.isClientSide) {
			world.setBlock(pos, newState, 11);
			if (player != null) {
				event.getItemStack().hurtAndBreak(1, player, (p_220040_1_) -> {
					p_220040_1_.broadcastBreakEvent(event.getHand());
				});
			}
		}

		event.setCanceled(true);
	}
}
