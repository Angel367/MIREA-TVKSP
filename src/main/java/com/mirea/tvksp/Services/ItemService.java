package com.mirea.tvksp.Services;

import com.mirea.tvksp.Entities.Item;
import com.mirea.tvksp.Repositories.ItemRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ItemService {

    private final ItemRepository itemRepository;

    public ItemService(ItemRepository itemRepository) {
        this.itemRepository = itemRepository;
    }

    public Item addItem(String name) {
        Item newItem = new Item(name);
        return itemRepository.save(newItem);
    }

    public List<Item> getAllItems() {
        return itemRepository.findAll();
    }
}