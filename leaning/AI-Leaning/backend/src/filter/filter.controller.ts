import { Body, Controller, Delete, Get, Post } from '@nestjs/common';
import { FilterService, FilterState } from './filter.service';

@Controller('filter')
export class FilterController {
  constructor(private readonly filterService: FilterService) {}

  @Get('schema')
  getSchema() {
    return this.filterService.getSchema();
  }

  @Get('state')
  getState() {
    return {
      filter: this.filterService.getState(),
      ...this.filterService.getResults(),
    };
  }

  @Post('apply')
  apply(@Body() body: FilterState) {
    this.filterService.applyFilter(body || {});
    return {
      filter: this.filterService.getState(),
      ...this.filterService.getResults(),
    };
  }

  @Post('reset')
  reset() {
    this.filterService.reset();
    return {
      filter: this.filterService.getState(),
      ...this.filterService.getResults(),
    };
  }

  @Get('bugs')
  getBugs() {
    return this.filterService.getBugs();
  }

  @Delete('bugs')
  clearBugs() {
    this.filterService.clearBugs();
    return { ok: true };
  }
}
